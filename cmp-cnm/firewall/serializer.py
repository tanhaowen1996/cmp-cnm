from rest_framework import serializers
from .models import Firewall

class FirewallSerializers(serializers.ModelSerializer):
    class Meta:
        model = Firewall
        fields = '__all__'