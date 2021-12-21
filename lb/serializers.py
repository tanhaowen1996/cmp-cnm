from rest_framework import serializers
from .models import LoadBalance, LoadBalancePath, \
    LoadBalanceMember, LoadBalanceListener, \
    LoadBalanceHost, SSL


class LoadBalanceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False),
    tenant_id = serializers.CharField(required=False),
    id = serializers.UUIDField(required=False),
    name = serializers.CharField(required=False),
    ip = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    subnet_id = serializers.UUIDField(required=False),
    port_id = serializers.UUIDField(required=False),
    provider = serializers.UUIDField(required=False),
    status = serializers.CharField(required=False)
    status_desc = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = LoadBalance
        fields = (
            'id',
            'name',
            'type',
            'ip',
            'subnet_id',
            'port_id',
            'provider',
            'status',
            'status_desc',
            'description',
            'tenant_id',
            'created_at'
        )
