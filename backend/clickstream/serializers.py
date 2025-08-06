from rest_framework import serializers
from .models import Clickstream

class ClickstreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clickstream
        fields = '__all__'
        read_only_fields = ['time', 'ip_address', 'user']
