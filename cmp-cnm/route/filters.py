from django_filters import (
    FilterSet,
    CharFilter)

class StaticRouteFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    ip_next_hop_address = CharFilter(field_name='ip_next_hop_address', lookup_expr='icontains')
    destination_subnet = CharFilter(field_name='destination_subnet', lookup_expr='icontains')
