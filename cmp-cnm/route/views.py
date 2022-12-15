from django.db.models import Q
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from lb.authentication import OSAuthentication
from .filters import StaticRouteFilter
from .models import StaticRoute
from .serializer import StaticRouteSerializers
from .cidr import Cidr
import logging

logger = logging.getLogger(__package__)


class StaticRouteViewSet(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet
                         ):
    authentication_classes = (OSAuthentication,)
    queryset = StaticRoute.objects.all()
    filterset_class = StaticRouteFilter
    serializer_class = StaticRouteSerializers

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            qs = qs.filter(Q(status='2') & Q(region=self.request.headers.get("Region")))
        if not self.request.user.is_staff:
            qs = qs.filter(Q(status='2') & Q(region=self.request.headers.get("Region")) &Q(tenant_id=self.request.tenant.get("id")))
        return qs

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(
                name=request.data['name'],
                region=request.headers.get("Region"),
                destination_subnet=request.data['destination_subnet'],
                ip_next_hop_address=request.data['ip_next_hop_address'],
                cluster_code=request.data['cluster_code'],
                tenant_id=request.tenant.get("id"),
                tenant_name=request.tenant.get('name'),
            )
            destination_subnet = request.data['destination_subnet'],
            ip_next_hop_address = request.data['ip_next_hop_address'],
            cluster_code = request.data['cluster_code'],
            destination_subnet = Cidr().Masker(destination_subnet[0], cluster_code[0])
            StaticRoute().create_route(destination_subnet, ip_next_hop_address[0], cluster_code[0])
            serializer.save(
                destination_subnet=destination_subnet,
                status='2'
            )
        except Exception as exc:
            logger.error(f"try creating static routing {serializer.validated_data}: {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            destination_subnet = instance.destination_subnet
            ip_next_hop_address = instance.ip_next_hop_address
            cluster_code = instance.cluster_code
            instance.destroy_routing(destination_subnet, ip_next_hop_address, cluster_code)
        except Exception as exc:
            logger.error(f"try destroying static routing {instance.name}: {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
