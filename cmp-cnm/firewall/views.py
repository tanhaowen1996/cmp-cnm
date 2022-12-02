from django.db.models import Q
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .filters import FirewallFilter
from lb.authentication import OSAuthentication
from .serializer import FirewallSerializers
import logging
from .models import Firewall

logger = logging.getLogger(__package__)

class FirewallViewSet(mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet
                         ):
    authentication_classes = (OSAuthentication,)
    queryset = Firewall.objects.all()
    filterset_class = FirewallFilter
    serializer_class = FirewallSerializers

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            qs = qs.filter(Q(status='2') & Q(region=self.request.headers.get("Region")))
        if not self.request.user.is_staff:
            qs = qs.filter(Q(status='2') & Q(region=self.request.headers.get("Region")) & Q(tenant_id=self.request.tenant.get("id")))
        return qs

    @action(detail=False,methods=['get'])
    def network_list(self,request, *args, **kwargs):
        network = Firewall().get_interface_network_list()
        return Response({'network':network}, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        try:
            rule_id = Firewall().create_rule_id()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except Exception as exc:
            logger.error({"detail": f"{exc}"})
            return Response({"detail": f"{exc}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(
                rule_id=rule_id,
                name=request.data['name'],
                region=request.headers.get("Region"),
                source_network=request.data['source_network'],
                destination_network=request.data['destination_network'],
                tenant_id=request.tenant.get("id"),
                tenant_name=request.tenant.get("name"),)
        try:
            rule_id = rule_id
            name = request.data['name']
            source_destination_network = Firewall().get_securityzone(request.data['source_network'],request.data['destination_network'])
            zone_source_network = source_destination_network['zone_source_network']
            zone_destination_network = source_destination_network['zone_destination_network']
            Firewall().create_security_policy(rule_id, name, zone_source_network, zone_destination_network)
        except Exception as exc:
            logger.error({"detail": f"{exc}"})
            return Response({"detail": f"{exc}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(
                status='2'
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            rule_id = instance.rule_id
            instance.delete_security_policy(rule_id)
        except Exception as exc:
            logger.error(f"try destroying firewall {instance.name}: {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_allow = request.data['is_allow']
        serializer = self.get_serializer(instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            instance.update_security_policy(instance.rule_id, instance.is_allow)
        except Exception as exc:
            logger.error(f"try update firewall {instance.name}: {exc}")
            return Response({
                "detail": f"{exc}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(
                is_allow=instance.is_allow
            )
        return Response(serializer.data)