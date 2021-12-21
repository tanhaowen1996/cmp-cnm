from django_filters import (
    Filter,
    FilterSet,
    CharFilter,
    ChoiceFilter,
    OrderingFilter,
    TypedChoiceFilter)
from distutils.util import strtobool
from .models import LoadBalance


class LoadBalanceFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    is_public = TypedChoiceFilter(
        choices=(('false', 'false'), ('true', 'true')),
        coerce=strtobool)

    class Meta:
        mode = LoadBalance
        filter = ('name', 'id', 'is_public')