from django_filters import (
    FilterSet,
    CharFilter,
    TypedChoiceFilter)
from distutils.util import strtobool
from .models import LoadBalance, LoadBalanceListener, \
    LoadBalanceMember


class LoadBalanceFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    tenant_id = CharFilter(field_name='tenant_id', lookup_expr='icontains')
    tenant_name = CharFilter(field_name='tenant_name', lookup_expr='icontains')

    class Meta:
        mode = LoadBalance
        filter = ('name', 'id', 'tenant_id', 'tenant_name')


class LoadBalanceListenerFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    protocol = CharFilter(field_name='protocol', lookup_expr='icontains')
    ld_id = CharFilter(field_name="lb_id", lookup_expr='icontains')

    class Meta:
        mode = LoadBalanceListener
        filter = ('name', 'id', 'protocol', 'lb_id')


class LoadBalanceMemberFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        mode = LoadBalanceMember
        filter = ('name', 'id', 'is_public')

