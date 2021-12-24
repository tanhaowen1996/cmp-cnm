from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from cmp_cnm.authentication import OSAuthentication
from .serializers import LoadBalanceSerializer
from .models import LoadBalance
from .filters import LoadBalanceFilter

from .citrixapi.session import NSMixin

# Create your views here.


class OSCommonModelMixin:
    update_serializer_class = None

    def get_serializer_class(self):
        return {
            'PUT': self.update_serializer_class
        }.get(self.request.method, self.serializer_class)


class LBViewSet(OSCommonModelMixin, viewsets.ModelViewSet):
    authentication_classes = (OSAuthentication,)
    filterset_class = LoadBalanceFilter
    serializer_class = LoadBalanceSerializer
    queryset = LoadBalance.objects.all()

    def create(self, request, *args, **kwargs):
        ns_conn = NSMixin.get_session()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        LoadBalance.create_cslb(ns_session=ns_conn, name=data['name'], address=data['ip'])
        return Response(status=status.HTTP_201_CREATED)



