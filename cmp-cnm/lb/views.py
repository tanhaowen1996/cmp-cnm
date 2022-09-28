from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .authentication import OSAuthentication
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from .serializers import LoadBalanceSerializer, LoadBalanceListenerSerializer, \
    LoadBalanceMemberSerializer, UpdateLoadBalanceSerializer
from .models import LoadBalance, LoadBalanceListener, LoadBalanceMember
from .filters import LoadBalanceFilter, LoadBalanceListenerFilter, LoadBalanceMemberFilter
from .citrixapi.session import NSMixin
from .citrixapi.client import citrix_save
from .radwareapi.session import RWMixin
from .radwareapi.client import apply_save
from cmp_cnm.settings import OS_REGION_MAWEI
from requests import exceptions
import logging
import openstack

logger = logging.getLogger(__package__)


class OSCommonModelMixin:
    update_serializer_class = None

    def get_serializer_class(self):
        return {
            'PUT': self.update_serializer_class
        }.get(self.request.method, self.serializer_class)


class LoadBalanceViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    """
        list:
        Get LB list

        create:
        Create LB
        需要传入参数如下：
        name lb名称
        net_type 网络类型
        network_id  负载均衡网络id
        description  描述

        retrieve:
        Get LB

        update:
        修改name和描述

        destroy:
        drop 负载均衡（需要保证负载均衡下无监听）
    """
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceFilter
    serializer_class = LoadBalanceSerializer
    update_serializer_class = UpdateLoadBalanceSerializer
    queryset = LoadBalance.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.headers.get("Region") == OS_REGION_MAWEI:
            qs = qs.filter(provider="citrix")
        else:
            qs = qs.filter(provider="radware")
        if not self.request.user.is_staff:
            qs = qs.filter(tenant_id=self.request.tenant.get("id"))
        return qs

    def create(self, request, *args, **kwargs):
        # ns_conn = NSMixin.get_session()
        try:
            rw_conn = RWMixin.get_session()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            serializer.save(
                name=data['name'],
                net_type=data.get('net_type', 'public'),
                status="create",
                tenant_id=request.tenant.get("id"),
                tenant_name=request.tenant.get('name'),
                description=data.get('description', None),
                network_id=data.get('network_id', None)
            )
        except Exception as e:
            logger.error(f"try creating loadbance ERROR: {e}")
            return Response({
                "detail": f"{e}"

            }, status=status.HTTP_400_BAD_REQUEST)
        if request.tenant.get("region_name") == OS_REGION_MAWEI:
            provider = "citrix"
        else:
            provider = "radware"
        if data.get('ip'):
            ipaddress = data['ip']
            port_id = None
            subnet_id = None
        else:
            try:
                port = LoadBalance.get_ip(request.os_conn, data.get('network_id'))
            except openstack.exceptions.HttpException as exc:
                logger.error(f"try creating openstack port {serializer.validated_data}: {exc}")
                lb = LoadBalance.objects.get(id=serializer.data['id'])
                lb.status = "filed"
                lb.save()
                return Response({
                    "detail": f"{exc}"

                }, status=status.HTTP_400_BAD_REQUEST)
            ipaddress = port.fixed_ips[0].get('ip_address')
            port_id = port.get('id')
            subnet_id = port.fixed_ips[0].get('subnet_id')
        if request.tenant.get("region_name") == OS_REGION_MAWEI:
            real_lb_identifier = data['name']
            # LoadBalance.create_lb(ns_session=ns_conn, name=data['name'], address=ipaddress)
        else:
            try:
                LoadBalance.create_rwlb(rw_session=rw_conn, lb_id=serializer.data['id'], address=ipaddress)
                real_lb_identifier = str(serializer.data['id'])
                apply_save(session=rw_conn)
            except Exception as e:
                logger.error(f"try creating loadbance ERROR: {e}")
                return Response({
                    "detail": f"{e}"

                }, status=status.HTTP_400_BAD_REQUEST)
        lb = LoadBalance.objects.get(id=serializer.data['id'])
        lb.ip = ipaddress
        lb.status = "up"
        lb.port_id = port_id
        lb.provider = provider
        lb.subnet_id = subnet_id
        lb.real_lb_identifier = real_lb_identifier
        lb.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete_citrix_lb(self, lb_id):
        ns_conn = NSMixin.get_session()
        try:
            lb = LoadBalance.objects.get(id=lb_id)
            if LoadBalanceListener.objects.filter(lb_id=lb_id):
                for listener in LoadBalanceListener.objects.filter(lb_id=lb_id):
                    if LoadBalanceMember.objects.filter(listener_id=listener.id):
                        for member in LoadBalanceMember.objects.filter(listener_id=listener.id):
                            member.delete()
                    if "-lbvs" in listener.name:
                        listener.delete_lb_listener(ns_session=ns_conn, name=listener.real_listener_identifier)
                    else:
                        listener.delete_csvs(ns_session=ns_conn, name=lb.name)
                    listener.delete()
        except Exception as e:
            logger.error(f"try delete loadbance ERROR: {e}")
            return Response({
                "detail": f"{e}"

            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            lb.delete_nslb(ns_conn, lb.real_lb_identifier)

    def delete_radware_lb(self, lb_id):
        rw_conn = RWMixin.get_session()
        try:
            lb = LoadBalance.objects.get(id=lb_id)
            if LoadBalanceListener.objects.filter(lb_id=lb_id):
                for listener in LoadBalanceListener.objects.filter(lb_id=lb_id):
                    if LoadBalanceMember.objects.filter(listener_id=listener.id):
                        for member in LoadBalanceMember.objects.filter(listener_id=listener.id):
                            LoadBalanceMember.delete_rw_member(rw_session=rw_conn,
                                                               member_id=member.real_member_identifier)
                            member.delete()
                    LoadBalanceListener.delete_rw_listener(rw_session=rw_conn,
                                                           lb_id=lb.real_lb_identifier,
                                                           port=listener.port,
                                                           listener_id=listener.real_listener_identifier,
                                                           protocol=listener.protocol)
                    listener.delete()
        except Exception as e:
            logger.error(f"try delete loadbance ERROR: {e}")
            return Response({
                "detail": f"{e}"

            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            LoadBalance.delete_rwlb(rw_session=rw_conn, lb_id=lb.real_lb_identifier)

    def destroy(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        rw_conn = RWMixin.get_session()
        instance = self.get_object()
        if instance.provider == "citrix":
            try:
                self.delete_citrix_lb(lb_id=instance.id)
                citrix_save(session=ns_conn)
            except nitro_exception as exc:
                logger.error(f"try Delete LoadBalance {instance.name} : {exc}")
                return Response({
                    "detail": f"{exc}"
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    request.os_conn.network.delete_port(instance.port_id)
                except openstack.exceptions.InvalidRequest as exc:
                    logger.error(f"try delete openstack port {instance.port_id}: {exc}")
                self.perform_destroy(instance)
                return Response("删除成功", status=status.HTTP_201_CREATED)
        else:
            try:
                self.delete_radware_lb(lb_id=instance.id)
                apply_save(session=rw_conn)
            except exceptions.Timeout as e:
                print(e)
            except exceptions.HTTPError as e:
                print(e)
            else:
                try:
                    request.os_conn.network.delete_port(instance.port_id)
                except openstack.exceptions.InvalidRequest as exc:
                    logger.error(f"try delete openstack port {instance.port_id}: {exc}")
                self.perform_destroy(instance)
                return Response("删除成功", status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['delete'])
    def delete_list(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        rw_conn = RWMixin.get_session()
        import ast
        lb_list = ast.literal_eval(request.data.get('lb_list'))
        # lb_list = request.POST.getlist('lb_id')
        if request.tenant.get("region_name") == OS_REGION_MAWEI:
            for lb_id in lb_list:
                lb = LoadBalance.objects.get(id=lb_id)
                try:
                   self.delete_citrix_lb(lb_id=lb_id)
                except nitro_exception as exc:
                    logger.error(f"try Delete LoadBalance {lb} : {exc}")
                    return Response({
                        "detail": f"{exc}"
                    }, status=status.HTTP_400_BAD_REQUEST)
                else:
                    try:
                        request.os_conn.network.delete_port(lb.port_id)
                    except openstack.exceptions.InvalidRequest as exc:
                        logger.error(f"try delete openstack port {lb.port_id}: {exc}")
                    LoadBalance.objects.filter(id=lb_id).delete()
            citrix_save(session=ns_conn)
            return Response("删除成功", status=status.HTTP_201_CREATED)
        else:
            for lb_id in lb_list:
                lb = LoadBalance.objects.get(id=lb_id)
                try:
                    self.delete_radware_lb(lb_id=lb.id)
                    apply_save(session=rw_conn)
                except exceptions.Timeout as e:
                    print(e)
                except exceptions.HTTPError as e:
                    print(e)
                else:
                    try:
                        request.os_conn.network.delete_port(lb.port_id)
                    except openstack.exceptions.InvalidRequest as exc:
                        logger.error(f"try delete openstack port {lb.port_id}: {exc}")
                    LoadBalance.objects.filter(id=lb_id).delete()
            apply_save(session=rw_conn)
            return Response("删除成功", status=status.HTTP_201_CREATED)


class LoadBalanceListenerViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    """
            list:
            Get LB_listener

            create:
            创建4层负载均衡
            需要传入参数如下：
            lb_id lb的id
            port  需要监听的端口
            protocol  4层负载均衡协议（TCP/UDP）
            algorithm  监听策略（轮询 ROUNDROBIN ，最小连接数 LEASTCONNECTION）

            retrieve:
            Get LB_listener

            update:
            无

            delete_v4:
            删除4层负载均衡监听
        """
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceListenerFilter
    serializer_class = LoadBalanceListenerSerializer
    queryset = LoadBalanceListener.objects.all()

    def create(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        rw_conn = RWMixin.get_session()
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            lb = LoadBalance.objects.get(id=data['lb_id'])
            lb_listener_name = lb.ip + ":" + str(data['port']) + "-" + data['protocol'] + "-lbvs"
            if LoadBalanceListener.objects.filter(lb_id=data['lb_id'], protocol=data['protocol'], port=data['port']):
                return Response({
                    "detail": f"已存在{lb.ip}-{data['protocol']}"
                }, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(
                lb_id=data['lb_id'],
                protocol=data['protocol'],
                port=data['port'],
                type="4层",
                algorithm=data.get('algorithm', 'ROUNDROBIN'),
                status="creat",
                name=lb_listener_name,
            )
        except Exception as e:
            logger.error(f"try serializer ERROR: {e}")
            return Response({
                "detail": f"{e}"
            }, status=status.HTTP_400_BAD_REQUEST)
        if lb.provider == "citrix":
            try:
                real_listener_identifier = lb_listener_name
                LoadBalanceListener.create_lb_listener(ns_session=ns_conn,
                                                       name=lb_listener_name,
                                                       address=lb.ip,
                                                       port=data['port'],
                                                       protocol=data['protocol'],
                                                       lbmethod=data.get('algorithm', 'ROUNDROBIN'))
                citrix_save(session=ns_conn)
            except Exception as exc:
                logger.error(f"try creating LoadBalance Listener {data['name']} : {exc}")
                lb_listener = LoadBalanceListener.objects.get(id=serializer.data['id'])
                lb_listener.status = "ERROR"
                lb_listener.save()
                return Response({
                    "detail": f"{exc}"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                real_listener_identifier = str(serializer.data['id'])
                LoadBalanceListener.create_rd_lb_listener(rw_session=rw_conn,
                                                          lb_id=lb.id,
                                                          listener_id=serializer.data['id'],
                                                          address=lb.ip,
                                                          port=data['port'],
                                                          protocol=data['protocol']
                                                          )
                apply_save(session=rw_conn)
            except Exception as e:
                logger.error(f"try creating LoadBalance Listener {data['name']} : {e}")
                lb_listener = LoadBalanceListener.objects.get(id=serializer.data['id'])
                lb_listener.status = "ERROR"
                lb_listener.save()
                return Response({
                    "detail": f"{e}"
                }, status=status.HTTP_400_BAD_REQUEST)
        try:
            lb_listener = LoadBalanceListener.objects.get(id=serializer.data['id'])
            lb_listener.name = lb_listener_name
            lb_listener.status = "0.00%"
            lb_listener.real_listener_identifier = real_listener_identifier
            lb_listener.save()
            serializer.data['name'] = lb_listener_name
            serializer.data['status'] = "0.00%"
            lb_listener = lb_listener.__dict__
            lb_listener["member_num"] = 0
            lb_listener["all_member"] = 0
            serializer = self.get_serializer(data=lb_listener)
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            logger.error(f"try update {data['name']} LoadBalance Listener database ERROR : {e}")
            lb_listener = LoadBalanceListener.objects.get(id=serializer.data['id'])
            lb_listener.status = "DATE ERROR"
            lb_listener.save()
            return Response({
                "detail": f"{e}"
            }, status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        rw_conn = RWMixin.get_session()
        instance = self.get_object()
        lb = LoadBalance.objects.get(id=instance.lb_id)
        if lb.provider == "citrix":
            try:
                if LoadBalanceMember.objects.filter(listener_id=instance.id):
                    for member in LoadBalanceMember.objects.filter(listener_id=instance.id):
                        member.delete()
                if "-lbvs" in instance.name:
                    instance.delete_lb_listener(ns_session=ns_conn, name=instance.real_listener_identifier)
                else:
                    instance.delete_csvs(ns_session=ns_conn, name=instance.name)
                citrix_save(session=ns_conn)
            except nitro_exception as exc:
                logger.error(f"try Delete LoadBalance Listener {instance.id} : {exc}")
                return Response({
                    "detail": f"{exc}"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                if LoadBalanceMember.objects.filter(listener_id=instance.id):
                    for member in LoadBalanceMember.objects.filter(listener_id=instance.id):
                        LoadBalanceMember.delete_rw_member(rw_session=rw_conn, member_id=member.real_member_identifier)
                        member.delete()
                lb = LoadBalance.objects.get(id=instance.lb_id)
                LoadBalanceListener.delete_rw_listener(rw_session=rw_conn,
                                                       lb_id=lb.real_lb_identifier,
                                                       port=instance.port,
                                                       listener_id=instance.real_listener_identifier,
                                                       protocol=instance.protocol)
                apply_save(session=rw_conn)
            except exceptions.Timeout as e:
                print(e)
            except exceptions.HTTPError as e:
                print(e)
        self.perform_destroy(instance)
        return Response("删除成功", status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['delete'])
    def delete_list(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        rw_conn = RWMixin.get_session()
        import ast
        listener_list = ast.literal_eval(request.data.get('listener_list'))
        if listener_list:
            listener = LoadBalanceListener.objects.get(id=listener_list[0])
            lb = LoadBalance.objects.get(id=listener.lb_id)
        else:
            return Response("missing parameter listener_list", status=status.HTTP_400_BAD_REQUEST)
        if lb.provider == "citrix":
            for listener_id in listener_list:
                listener = LoadBalanceListener.objects.get(id=listener_id)
                try:
                    if LoadBalanceMember.objects.filter(listener_id=listener.id):
                        for member in LoadBalanceMember.objects.filter(listener_id=listener.id):
                            member.delete()
                    if "-lbvs" in listener.name:
                        listener.delete_lb_listener(ns_session=ns_conn, name=listener.real_listener_identifier)
                    else:
                        listener.delete_csvs(ns_session=ns_conn, name=listener.name)
                except nitro_exception as exc:
                    logger.error(f"try Delete LoadBalance Listener {listener.id} : {exc}")
                    return Response({
                        "detail": f"{exc}"
                    }, status=status.HTTP_400_BAD_REQUEST)
                LoadBalanceListener.objects.filter(id=listener.id).delete()
            citrix_save(session=ns_conn)
        else:
            for listener_id in listener_list:
                listener = LoadBalanceListener.objects.get(id=listener_id)
                try:
                    if LoadBalanceMember.objects.filter(listener_id=listener.id):
                        for member in LoadBalanceMember.objects.filter(listener_id=listener.id):
                            LoadBalanceMember.delete_rw_member(rw_session=rw_conn,
                                                               member_id=member.real_member_identifier)
                            member.delete()
                    lb = LoadBalance.objects.get(id=listener.lb_id)
                    LoadBalanceListener.delete_rw_listener(rw_session=rw_conn,
                                                           lb_id=lb.real_lb_identifier,
                                                           port=listener.port,
                                                           listener_id=listener.real_listener_identifier,
                                                           protocol=listener.protocol)
                except exceptions.Timeout as e:
                    print(e)
                except exceptions.HTTPError as e:
                    print(e)
                LoadBalanceListener.objects.filter(id=listener.id).delete()
            apply_save(session=rw_conn)
        return Response("删除成功", status=status.HTTP_201_CREATED)

    def list_page(self, qs):
        queryset = self.filter_queryset(qs)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return serializer

        serializer = self.get_serializer(queryset, many=True)
        return serializer

    def list(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        rw_conn = RWMixin.get_session()
        qs = super().get_queryset()
        if not (request.GET.get('lb_id') or request.data.get('lb_id')):
            return Response("missing parameter lb_id", status=status.HTTP_400_BAD_REQUEST)
        else:
            qs = qs.filter(lb_id=request.GET.get('lb_id', request.data.get('lb_id')))
        serializer = self.list_page(qs)
        lb = LoadBalance.objects.get(id=request.GET.get('lb_id', request.data.get('lb_id')))
        if lb.provider == "citrix":
            try:
                for listener in serializer.data:
                    if not listener.get('real_listener_identifier'):
                        continue
                    ns_listener, ns_members = LoadBalanceListener.get_status(ns_session=ns_conn,
                                                                             name=listener.get(
                                                                                 'real_listener_identifier'))
                    if int(ns_listener.totalservices):
                        stat = format(float(format(float
                                                   (ns_listener.activeservices) / float(ns_listener.totalservices),
                                                   '.4f')
                                            ) * 100, '.2f') + "%"
                    else:
                        stat = "0.00%"
                    all_member = []
                    for ns_member in ns_members:
                        mem = {'name': ns_member.servicename, 'status': ns_member.curstate}
                        all_member.append(mem)
                    LoadBalanceListener.objects.filter(id=listener.get('id')).update(
                        all_member=all_member,
                        member_num=int(ns_listener.totalservices),
                        status=stat
                    )
                serializer = self.list_page(qs)
            except Exception as e:
                logger.error(f"获取Listener错误：{e}")
        else:
            try:
                for listener in serializer.data:
                    if not listener.get('real_listener_identifier'):
                        continue
                    members = LoadBalanceMember.objects.filter(listener_id=listener.get("id"))
                    state_up = 0
                    all = 0
                    all_member = []
                    for member in members:
                        if not listener.get('real_listener_identifier'):
                            continue
                        real_member = LoadBalanceMember.get_info_member(rw_session=rw_conn,
                                                                        member_id=member.real_member_identifier)
                        all = all + 1
                        if real_member[0].get("State") == 2:
                            state_up = state_up + 1
                            mem = {'name': real_member[0].get("IpAddr"), 'status': "UP"}
                        else:
                            mem = {'name': real_member[0].get("IpAddr"), 'status': "DOWN"}
                        all_member.append(mem)
                    if all == 0:
                        stat = "0.00%"
                    else:
                        stat = format(float(format(float
                                                   (state_up) / float(all), '.4f')
                                            ) * 100, '.2f') + "%"
                    LoadBalanceListener.objects.filter(id=listener.get('id')).update(
                        all_member=all_member,
                        member_num=all,
                        status=stat
                    )
                serializer = self.list_page(qs)
            except Exception as e:
                logger.error(f"获取Listener错误：{e}")
        return self.get_paginated_response(serializer.data)


class LoadBalanceMemberViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    """
            list:
            需要传入listener参数
            Get LB Member

            add_mamber:
            添加 4层 LB member
            需要传入参数如下：
            listener_id  4层负载均衡监听的id
            ip    成员的地址
            port  成员的端口
            weight  成员的权重

            retrieve:
            Get LB path

            update:
            修改负载均衡成员权重

            destroy:
            删除4层负载均衡监听成员
        """
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceMemberFilter
    serializer_class = LoadBalanceMemberSerializer
    queryset = LoadBalanceMember.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.GET.get('listener_id'):
            return qs
        qs = qs.filter(listener_id=self.request.GET.get('listener_id'))
        return qs

    @action(detail=False, methods=['post'])
    def add_member(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        rw_conn = RWMixin.get_session()
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            member_list = LoadBalanceMember.objects.filter(listener_id=data['listener_id'])
            if member_list.filter(ip=data['ip'], port=data['port']):
                return Response({
                    "detail": f"已存在成员{data['ip']}端口{data['port']}"
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save(
                listener_id=data['listener_id'],
                ip=data['ip'],
                port=data['port'],
                weight=data.get('weight', 1)
            )
        except Exception as e:
            logger.error(f"try serializer ERROR: {e}")
            LoadBalanceMember.objects.get(id=serializer.data['id']).delete()
            return Response({
                "detail": f"{e}"

            }, status=status.HTTP_400_BAD_REQUEST)
        listener = LoadBalanceListener.objects.get(id=data['listener_id'])
        lb = LoadBalance.objects.get(id=listener.lb_id)
        if lb.provider == "citrix":
            try:
                protocol = listener.protocol
                lbvs_name = listener.real_listener_identifier
                LoadBalanceMember.add_member(ns_session=ns_conn,
                                             address=data['ip'],
                                             port=data['port'],
                                             weight=data.get('weight', 1),
                                             protocol=protocol,
                                             vs_name=lbvs_name)
                real_member_identifier = data['ip'] + ":" + str(data['port']) + "-" + protocol
                citrix_save(session=ns_conn)
            except Exception as exc:
                logger.error(f"try add LoadBalance member v4 : {exc}")
                LoadBalanceMember.objects.get(id=serializer.data['id']).delete()
                return Response({
                    "detail": f"{exc}"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                LoadBalanceMember.add_rw_member(rw_session=rw_conn,
                                                ip=data['ip'],
                                                port=data['port'],
                                                member_id=serializer.data['id'],
                                                weight=data.get('weight', 1),
                                                listener_id=data['listener_id'])
                real_member_identifier = serializer.data['id']
                apply_save(session=rw_conn)
            except Exception as e:
                logger.error(f"try add LoadBalance member ERROR : {e}")
                LoadBalanceMember.objects.get(id=serializer.data['id']).delete()
                return Response({
                    "detail": f"{e}"
                }, status=status.HTTP_400_BAD_REQUEST)

        lb_member = LoadBalanceMember.objects.get(id=serializer.data['id'])
        lb_member.real_member_identifier = real_member_identifier
        lb_member.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        rw_conn = RWMixin.get_session()
        instance = self.get_object()
        listener = LoadBalanceListener.objects.get(id=instance.listener_id)
        lb = LoadBalance.objects.get(id=listener.lb_id)
        if not instance.real_member_identifier:
            self.perform_destroy(instance)
            return Response("删除成功", status=status.HTTP_201_CREATED)
        if lb.provider == "citrix":
            try:
                lbvs_name = listener.real_listener_identifier
                member_name = instance.real_member_identifier
                instance.delete_lb_member(ns_conn, lbvs_name=lbvs_name, member_name=member_name)
                citrix_save(session=ns_conn)
            except nitro_exception as exc:
                logger.error(f"try Delete LoadBalance {instance.id} : {exc}")
                return Response({
                    "detail": f"{exc}"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                LoadBalanceMember.delete_rw_member(rw_session=rw_conn, member_id=instance.real_member_identifier)
                apply_save(session=rw_conn)
            except Exception as e:
                logger.error(f"try Delete LoadBalance {instance.id} : {e}")
                return Response({
                    "detail": f"{e}"
                }, status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response("删除成功", status=status.HTTP_201_CREATED)

    def list_page(self, qs):
        queryset = self.filter_queryset(qs)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return serializer

        serializer = self.get_serializer(queryset, many=True)
        return serializer

    def list(self, request, *args, **kwargs):
        qs = super().get_queryset()
        if not (request.GET.get('listener_id') or request.data.get('listener_id')):
            return Response("missing parameter listener_id", status=status.HTTP_400_BAD_REQUEST)
        else:
            qs = qs.filter(listener_id=request.GET.get('listener_id', request.data.get('listener_id')))
        serializer = self.list_page(qs)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        instance = self.get_object()
        try:
            listener = LoadBalanceListener.objects.get(id=instance.listener_id)
            lbvs_name = listener.name
            member_name = instance.ip + ":" + str(instance.port) + "-" + listener.protocol
            instance.update_lb_member(ns_conn,
                                      lbvs_name,
                                      member_name,
                                      request.data['ip'],
                                      request.data['port'],
                                      request.data['weight'],
                                      listener.protocol
                                      )
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
        except nitro_exception as exc:
            logger.error(f"try update LoadBalance  members {instance.ip} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def sync_member(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        rw_conn = RWMixin.get_session()
        listeners = LoadBalanceListener.objects.all()
        try:
            for listener in listeners:
                members = LoadBalanceMember.objects.filter(listener_id=listener.id)
                members.delete()
                lb = LoadBalance.objects.get(id=listener.lb_id)
                if lb.provider == "citrix":
                    ns_members = LoadBalanceMember.get_ns_members(ns_session=ns_conn,
                                                                  name=listener.real_listener_identifier)
                    if ns_members:
                        for ns_member in ns_members:
                            LoadBalanceMember.objects.create(
                                listener_id=listener.id,
                                ip=ns_member.ipv46,
                                port=ns_member.port,
                                weight=int(ns_member.weight),
                                real_member_identifier=ns_member.servicename
                            )
                else:
                    rw_members = LoadBalanceMember.get_rw_members(rw_session=rw_conn,
                                                                  listener_id=listener.real_listener_identifier)
                    if rw_members:
                        for rw_member in rw_members:
                            real_member = LoadBalanceMember.get_info_member(rw_session=rw_conn,
                                                                            member_id=rw_member.get("ServIndex"))
                            LoadBalanceMember.objects.create(
                                listener_id=listener.id,
                                ip=real_member[0].get("IpAddr"),
                                port=real_member[0].get("SwitchPort"),
                                weight=1,
                                real_member_identifier=rw_member.get("ServIndex"),
                            )
        except Exception as e:
            logger.error(f"同步失败: {e} {listener}")
            return Response({
                "detail": f"{e}"
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response("同步成功", status=status.HTTP_201_CREATED)

