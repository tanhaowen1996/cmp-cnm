from django.contrib import admin
from .models import LoadBalance, \
    LoadBalanceMember, \
    LoadBalanceListener


@admin.register(LoadBalance)
class LoadBalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'net_type', 'ip', 'network_id', 'subnet_id',
                    'port_id', 'provider', 'status',
                    'description', 'tenant_id', 'tenant_name', 'created_at')


@admin.register(LoadBalanceMember)
class LoadBalanceMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'listener_id', 'ip', 'port',
                    'weight', 'created_at')


@admin.register(LoadBalanceListener)
class LoadBalanceListenerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lb_id', 'protocol', 'port', 'type',
                    'algorithm', 'persistence', 'status', 'created_at')
