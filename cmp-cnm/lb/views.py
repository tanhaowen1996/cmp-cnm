from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from cmp_cnm.authentication import OSAuthentication
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from .serializers import LoadBalanceSerializer, LoadBalanceListenerSerializer, \
    LoadBalanceHostSerializer, LoadBalancePathSerializer, \
    LoadBalanceMemberSerializer, SSLSerializer
from .models import LoadBalance, LoadBalanceListener, LoadBalanceHost, \
    LoadBalancePath, LoadBalanceMember, SSL
from .filters import LoadBalanceFilter, LoadBalanceListenerFilter, LoadBalanceHostFilter, \
    LoadBalancePathFilter, LoadBalanceMemberFilter, SSLFilter
from .citrixapi.session import NSMixin
import logging
from datetime import datetime

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
        ip  负载均衡ip地址（非网段）
        description  描述

        retrieve:
        Get LB

        update:
        无

        destroy:
        drop 负载均衡（需要保证负载均衡下无监听）
    """
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceFilter
    serializer_class = LoadBalanceSerializer
    queryset = LoadBalance.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(tenant_id=self.request.account_info['tenantId'])
        return qs

    def create(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            LoadBalance.create_cslb(ns_session=ns_conn, name=data['name'], address=data['ip'])
        except nitro_exception as exc:
            logger.error(f"try creating LoadBalance {data['name']} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            lb = LoadBalance.get_cslb(ns_session=ns_conn, name=data['name'])
            if lb.status:
                lb_status = "up"
            else:
                lb_status = "down"
            serializer.save(
                name=data['name'],
                ip=data['ip'],
                net_type=data['net_type'],
                status=lb_status,
                tenant_id=request.account_info.get('tenantId'),
                tenant_name=request.account_info.get('tenantName'),
                description=data['description'],
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        instance = self.get_object()
        try:
            if LoadBalanceListener.objects.filter(lb_id=instance.id):
                return Response(f"ERROR: You must delete {instance.id}: Listener", status=status.HTTP_400_BAD_REQUEST)
            instance.delete_cslb(ns_conn, instance.name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {instance.name} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_201_CREATED)


class LoadBalanceListenerViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    """
            list:
            Get LB_listener

            create_v4:
            创建4层负载均衡
            需要传入参数如下：
            lb_id lb的id
            port  需要监听的端口
            protocol  4层负载均衡协议（TCP/UDP）
            algorithm  监听策略（轮询 ROUNDROBIN ，最小连接数 LEASTCONNECTION）

            create_v7:
            创建7层负载均衡
            需要传入参数如下：
            lb_id lb的id
            port  需要监听的端口
            protocol  7层负载均衡协议（HTTP/HTTPS）
            ssl  （HTTPS时需要传人证书名称）

            retrieve:
            Get LB_listener

            update:
            无

            delete_v4:
            删除4层负载均衡监听

            delete_v7:
            删除4层负载均衡监听

            listener_list_v4:
            需要传入lb_id 参数

            listener_list_v7:
            需要传入lb_id 参数
        """
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceListenerFilter
    serializer_class = LoadBalanceListenerSerializer
    queryset = LoadBalanceListener.objects.all()

    @action(detail=False, methods=['post'])
    def create_v4(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            lb = LoadBalance.objects.get(id=data['lb_id'])
            lb_listener_name = lb.ip + ":" + str(data['port']) + "-" + data['protocol']
            LoadBalanceListener.create_lb_listener_v4(ns_session=ns_conn,
                                                      name=lb_listener_name,
                                                      address=lb.ip,
                                                      port=data['port'],
                                                      protocol=data['protocol'],
                                                      lbmethod=data['algorithm'])
        except nitro_exception as exc:
            logger.error(f"try creating LoadBalance {data['name']} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(
                name=lb_listener_name,
                lb_id=data['lb_id'],
                protocol=data['protocol'],
                port=data['port'],
                type="4层",
                pip=lb.net_type,
                algorithm=data['algorithm'],
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post'])
    def create_v7(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            lb = LoadBalance.objects.get(id=data['lb_id'])
            lb_listener_name = lb.ip + ":" + str(data['port']) + "-" + data['protocol']
            LoadBalanceListener.create_lb_listener_v7(ns_session=ns_conn,
                                                      name=lb_listener_name,
                                                      address=lb.ip,
                                                      port=data['port'],
                                                      protocol=data['protocol'])
            if data['protocol'] == "HTTPS":
                ssl = data['ssl']
                LoadBalanceListener.add_ssl(ns_conn, ssl_name=ssl, listener_name=lb_listener_name)
        except nitro_exception as exc:
            logger.error(f"try creating LoadBalance {data['name']} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(
                name=lb_listener_name,
                lb_id=data['lb_id'],
                protocol=data['protocol'],
                port=data['port'],
                type="7层",
                pip=lb.net_type
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def delete_v4(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        instance = self.get_object()
        try:
            instance.delete_lb_listenet_v4(ns_session=ns_conn, name=instance.name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {instance.id} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def delete_v7(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        instance = self.get_object()
        try:
            if instance.delete_lb_listenet_v7_check(ns_session=ns_conn, name=instance.name):
                return Response(f"ERROR: You must delete {instance.id}: Host", status=status.HTTP_400_BAD_REQUEST)
            instance.delete_lb_listenet_v7(ns_session=ns_conn, name=instance.name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {instance.id} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_201_CREATED)

    def list_page(self, qs):
        queryset = self.filter_queryset(qs)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return serializer

        serializer = self.get_serializer(queryset, many=True)
        return serializer

    @action(detail=False, methods=['get'])
    def listener_list_v4(self, request, *args, **kwargs):
        qs = super().get_queryset()
        if not request.GET.get('lb_id'):
            qs = qs.filter(Q(protocol="TCP") | Q(protocol="UDP"))
        else:
            qs = qs.filter(Q(lb_id=request.GET.get('lb_id')) & (Q(protocol="TCP") | Q(protocol="UDP")))
        serializer = self.list_page(qs)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def listener_list_v7(self, request, *args, **kwargs):
        qs = super().get_queryset()
        if not request.GET.get('lb_id'):
            qs = qs.filter(Q(protocol="HTTP") | Q(protocol="HTTPS"))
        else:
            qs = qs.filter(Q(lb_id=request.GET.get('lb_id')) & (Q(protocol="HTTP") | Q(protocol="HTTPS")))
        serializer = self.list_page(qs)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoadBalanceHostViewSet(viewsets.ModelViewSet):
    """
        list:
        需要传入 listener_id 参数
        Get LB host

        create:
        Create LB host
        需要传入参数如下：
        host 域名
        match_type 匹配模式（目前支持：包含：CONTAINS 等于：EQ）
        listener_id  监听的id

        retrieve:
        Get LB HOST

        update:
        无

        destroy:
        drop 负载均衡域名
    """
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceHostFilter
    serializer_class = LoadBalanceHostSerializer
    queryset = LoadBalanceHost.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.GET.get('listener_id'):
            return qs
        qs = qs.filter(listener_id=self.request.GET.get('listener_id'))

        return qs

    def create(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            listener = LoadBalanceListener.objects.get(id=data['listener_id'])
            host_name = listener.name + "-" + data['host']
            LoadBalanceHost.create_lb_host(ns_session=ns_conn,
                                           name=host_name,
                                           host=data['host'],
                                           match_type=data['match_type'],
                                           listener=listener.name,
                                           protocol=listener.protocol)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {data['host']} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(
                listener_id=data['listener_id'],
                host=data['host'],
                match_type=data['match_type'],
                name=host_name
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        instance = self.get_object()
        try:
            if LoadBalancePath.objects.filter(host_id=instance.id):
                return Response(f"ERROR: You must delete {instance.id}: Path", status=status.HTTP_400_BAD_REQUEST)
            listener = LoadBalanceListener.objects.get(id=instance.listener_id)
            lb_name = listener.name
            instance.delete_lb_host(ns_conn, lb_name=lb_name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {instance.id} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_201_CREATED)


class LoadBalancePathViewSet(viewsets.ModelViewSet):
    """
        list:
        需要传入 host_id 参数
        Get LB path

        create:
        Create LB path
        需要传入参数如下：
        host_id 域名id
        path   路径（默认为：/）
        match_type 匹配模式（目前支持：包含：CONTAINS 等于：EQ）
        algorithm  监听策略（轮询 ROUNDROBIN ，最小连接数 LEASTCONNECTION）

        retrieve:
        Get LB path

        update:
        无

        destroy:
        drop 负载均衡路径
    """
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalancePathFilter
    serializer_class = LoadBalancePathSerializer
    queryset = LoadBalancePath.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.GET.get('host_id'):
            return qs
        qs = qs.filter(host_id=self.request.GET.get('host_id'))

        return qs

    def create(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            host = LoadBalanceHost.objects.get(id=data['host_id'])
            listener = LoadBalanceListener.objects.get(id=host.listener_id)
            path_name = host.name
            path = LoadBalancePath.create_lb_path(ns_conn,
                                           listener=listener.name,
                                           name=path_name,
                                           match_type=data['match_type'],
                                           host_match_type=host.match_type,
                                           protocol=listener.protocol,
                                           lbmethod=data['algorithm'],
                                           lb_host=host.host,
                                           path=data['path'])
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {data['path']} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(
                host_id=data['host_id'],
                path=data['path'],
                algorithm=data['algorithm'],
                match_type=data['match_type'],
                name=path
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        instance = self.get_object()
        try:
            host = LoadBalanceHost.objects.get(id=instance.host_id)
            listener = LoadBalanceListener.objects.get(id=host.listener_id)
            lb_name = listener.name
            instance.delete_lb_path(ns_conn, lb_name=lb_name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {instance.id} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_201_CREATED)


class LoadBalanceMemberViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    """
            list:
            需要传入p_id 参数
            Get LB Member

            add_mamber_v4:
            添加 4层 LB member
            需要传入参数如下：
            p_id  4层负载均衡监听的id
            ip    成员的地址
            port  成员的端口
            weight  成员的权重

            add_mamber_v7:
            添加 7层 LB member
            需要传入参数如下：
            p_id  7层负载均衡的path id
            ip    成员的地址
            port  成员的端口
            weight  成员的权重

            retrieve:
            Get LB path

            update:
            无

            delete_v4:
            删除4层负载均衡监听成员

            delete_v7:
            删除4层负载均衡监听成员
        """
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceMemberFilter
    serializer_class = LoadBalanceMemberSerializer
    queryset = LoadBalanceMember.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.GET.get('p_id'):
            return qs
        qs = qs.filter(p_id=self.request.GET.get('p_id'))

        return qs

    @action(detail=False, methods=['post'])
    def add_member_v4(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            listener = LoadBalanceListener.objects.get(id=data['p_id'])
            protocol = listener.protocol
            lbvs_name = listener.name + "-lbvs"
            LoadBalanceMember.add_member(ns_session=ns_conn,
                                         address=data['ip'],
                                         port=data['port'],
                                         weight=data['weight'],
                                         protocol=protocol,
                                         vs_name=lbvs_name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {data['']} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(
                p_id=data['p_id'],
                ip=data['ip'],
                port=data['port'],
                weight=data['weight']
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post'])
    def add_member_v7(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            path = LoadBalancePath.objects.get(id=data['p_id'])
            host = LoadBalanceHost.objects.get(id=path.host_id)
            listener = LoadBalanceListener.objects.get(id=host.listener_id)
            lbvs_name = path.name + "-lbvs"
            protocol = listener.protocol
            LoadBalanceMember.add_member(ns_session=ns_conn,
                                         address=data['ip'],
                                         port=data['port'],
                                         weight=data['weight'],
                                         protocol=protocol,
                                         vs_name=lbvs_name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {data['']} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(
                p_id=data['p_id'],
                ip=data['ip'],
                port=data['port'],
                weight=data['weight']
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['delete'])
    def delete_v4(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        instance = self.get_object()
        try:
            listener = LoadBalanceListener.objects.get(id=instance.p_id)
            lbvs_name = listener.name + "-lbvs"
            member_name = instance.ip + ":" + str(instance.port) + "-" + listener.protocol
            instance.delete_lb_member(ns_conn, lbvs_name=lbvs_name, member_name=member_name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {instance.id} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'])
    def delete_v7(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        instance = self.get_object()
        try:
            path = LoadBalancePath.objects.get(id=instance.p_id)
            host = LoadBalanceHost.objects.get(id=path.host_id)
            listener = LoadBalanceListener.objects.get(id=host.listener_id)
            lbvs_name = path.name + "-lbvs"
            member_name = instance.ip + ":" + str(instance.port) + "-" + listener.protocol
            instance.delete_lb_member(ns_conn, lbvs_name=lbvs_name, member_name=member_name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {instance.id} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_201_CREATED)


class SSLViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    """
        list:
        Get SSL证书

        create:
        Create SSL证书
        需要传入参数如下：
        name ssl证书名称
        cert ca证书
        pkey 证书key
        scope  证书权限（私有/公有）

        retrieve:
        Get LB

        update:
        无

        destroy:
        drop SSL证书
    """

    authentication_classes = (OSAuthentication,)
    filterset_class = SSLFilter
    serializer_class = SSLSerializer
    queryset = SSL.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(tenant_id=self.request.account_info['tenantId'])
        return qs

    def create(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            SSL.create_ssl(ns_conn, data['name'], data['cert'], data['pkey'])
        except nitro_exception as exc:
            logger.error(f"try Create SSL {data['name']} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            ssl = SSL.get_ssl(ns_conn, data['name'])
            GMT_FORMAT = "%b %d %H:%M:%S %Y GMT"

            serializer.save(
                name=data['name'],
                cert=data['cert'],
                pkey=data['pkey'],
                scope=data['scope'],
                cert_type="SVR",
                domain=ssl.sandns,
                status=ssl.status,
                cert_begin_time=datetime.strptime(ssl.clientcertnotbefore, GMT_FORMAT),
                cert_end_time=datetime.strptime(ssl.clientcertnotafter, GMT_FORMAT),
                tenant_id=request.account_info.get('tenantId'),
                tenant_name=request.account_info.get('tenantName'),
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        instance = self.get_object()
        try:
            instance.delete_ssl(ns_conn, instance.name)
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {instance.name} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_201_CREATED)

