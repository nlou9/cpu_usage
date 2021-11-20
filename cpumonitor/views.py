from typing import List
from .models import CpuUsage
from rest_framework import generics
from rest_framework import viewsets
from .serializers import CpuUsageSerializer
from django.views.generic import ListView, DetailView

"""
create API view
"""
class CpuUsageCreate(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CpuUsage.objects.all()
    serializer_class = CpuUsageSerializer

"""
Get CPU record with server_id
"""

class CpuUsageList(generics.ListAPIView):
    """
    List All 
    """
    lookup_field = "server_id"
    serializer_class = CpuUsageSerializer

    def get_queryset(self):
        serverid = self.kwargs.get(self.lookup_field)
        usages = CpuUsage.objects.filter(server_id=serverid)
        return usages 

"""
Get CPU range with server_id and time range
"""
class CpuUsageTimeRangeList(generics.ListAPIView):

    lookup_field = "server_id"
    start = "start"
    end = "end"
    serializer_class = CpuUsageSerializer

    def get_queryset(self):
        serverid = self.kwargs.get(self.lookup_field)
        start = self.kwargs.get(self.start)
        end = self.kwargs.get(self.end)      
        range_usages = CpuUsage.objects.filter(server_id=serverid,created__gte=start,created__lte=end)
        return range_usages  