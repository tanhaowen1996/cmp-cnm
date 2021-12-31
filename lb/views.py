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
        Get list

        create:
        Create instance

        retrieve:
        Get instance

        update:
        Update instance

        destroy:
        drop instance

        tenants:
        set related tenant list for instance

        release:
        remove current tenant from the tenant list of instance

        verbosity:
        Get instance detail info
    """
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceFilter
    serializer_class = LoadBalanceSerializer
    queryset = LoadBalance.objects.all()

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
            instance.delete_cslb(ns_conn, request.data['name'])
        except nitro_exception as exc:
            logger.error(f"try Delete LoadBalance {instance.name} : {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_201_CREATED)


class LoadBalanceListenerViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
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


class LoadBalanceHostViewSet(viewsets.ModelViewSet):
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceHostFilter
    serializer_class = LoadBalanceHostSerializer
    queryset = LoadBalanceHost.objects.all()

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
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalancePathFilter
    serializer_class = LoadBalancePathSerializer
    queryset = LoadBalancePath.objects.all()

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
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceMemberFilter
    serializer_class = LoadBalanceMemberSerializer
    queryset = LoadBalanceMember.objects.all()

    @action(detail=False, methods=['post'])
    def add_mamber_v4(self, request, *args, **kwargs):
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
    def add_mamber_v7(self, request, *args, **kwargs):
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
    authentication_classes = (OSAuthentication,)
    filterset_class = SSLFilter
    serializer_class = SSLSerializer
    queryset = SSL.objects.all()

    def create(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
