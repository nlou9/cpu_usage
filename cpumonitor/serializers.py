from rest_framework import serializers
from .models import CpuUsage
"""
Use ModelSerializer to convert any model to serialized JSON object
"""
class CpuUsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CpuUsage
        fields = [
            "server_id",
            "sys_usage",
            "user_usage",
            "idle", 
            "created"
        ]
        extra_kwargs= {
            "created": {"required":False},
        }


