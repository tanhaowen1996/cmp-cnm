from rest_framework import serializers

from .models import StaticRoute

class StaticRouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaticRoute
        fields = '__all__'