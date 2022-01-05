from django.contrib import admin
from .models import LoadBalance, \
    LoadBalanceHost, \
    LoadBalanceMember, \
    LoadBalanceListener, \
    LoadBalancePath, \
    SSL


@admin.register(LoadBalance)
class LoadBalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'net_type', 'ip', 'subnet_id',
                    'port_id', 'provider', 'status', 'status_desc',
                    'description', 'tenant_id', 'tenant_name', 'created_at')


@admin.register(LoadBalanceHost)
class LoadBalanceHostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listener_id', 'host',
                    'match_type', 'created_at')


@admin.register(LoadBalanceMember)
class LoadBalanceMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_id', 'ip', 'port',
                    'weight', 'created_at')


@admin.register(LoadBalanceListener)
class LoadBalanceListenerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lb_id', 'protocol', 'port', 'type', 'pip',
                    'ssl_id', 'algorithm', 'status', 'status_desc',
                    'created_at')


@admin.register(LoadBalancePath)
class LoadBalancePathAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'host_id', 'path', 'algorithm',
                    'match_type', 'created_at')


@admin.register(SSL)
class SSLAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scope', 'cert_type', 'domain',
                    'cert', 'pkey', 'status', 'cert_begin_time',
                    'cert_end_time', 'tenant_id',
                    'tenant_name', 'created_at')
