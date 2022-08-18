from rest_framework import serializers
from .models import LoadBalance, \
    LoadBalanceMember, LoadBalanceListener


class LoadBalanceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    ip = serializers.CharField(required=False)
    net_type = serializers.CharField(required=False)
    network_id = serializers.UUIDField(required=False)
    subnet_id = serializers.UUIDField(required=False)
    port_id = serializers.UUIDField(required=False)
    provider = serializers.UUIDField(required=False)
    status = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    tenant_id = serializers.CharField(required=False)
    tenant_name = serializers.CharField(required=False)

    class Meta:
        model = LoadBalance
        fields = (
            'id',
            'name',
            'net_type',
            'ip',
            'network_id',
            'subnet_id',
            'port_id',
            'provider',
            'status',
            'description',
            'tenant_id',
            'tenant_name',
            'created_at'
        )


class LoadBalanceListenerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    lb_id = serializers.UUIDField(required=False)
    protocol = serializers.CharField(required=False)
    port = serializers.IntegerField(required=False)
    type = serializers.CharField(required=False)
    algorithm = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    member_num = serializers.IntegerField(required=False)
    all_member = serializers.JSONField(required=False)

    class Meta:
        model = LoadBalanceListener
        fields = (
            'id',
            'name',
            'lb_id',
            'protocol',
            'port',
            'type',
            'algorithm',
            'status',
            'member_num',
            'all_member',
        )


class LoadBalanceMemberSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    listener_id = serializers.UUIDField(required=False)
    ip = serializers.CharField(required=False)
    port = serializers.IntegerField(required=False)
    weight = serializers.IntegerField(required=False)

    class Meta:
        model = LoadBalanceMember
        fields = (
            'id',
            'listener_id',
            'ip',
            'port',
            'weight'
        )
