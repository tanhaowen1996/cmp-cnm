from django_filters import (
    FilterSet,
    CharFilter)

class FirewallFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    source_network = CharFilter(field_name='source_network', lookup_expr='icontains')
    destination_network = CharFilter(field_name='destination_network', lookup_expr='icontains')
