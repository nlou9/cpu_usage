from .models import CpuUsage
from rest_framework import generics
from .serializers import CpuUsageSerializer
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import logging

logger = logging.getLogger(__name__)

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
        if isinstance(serverid,int):
            usages = CpuUsage.objects.filter(server_id=serverid)
        else:
            raise TypeError("server type is not integer")
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
        #"2021-11-22T00:06:01.909068Z"   
        try:
            d1 = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S.%fZ')
            d2 = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError as e:  
            logger.info(e)
            raise ValueError("Incorrect datetime format")
        if d1 > d2:
            raise ValueError("End time should not be late than start time.")
        range_usages = CpuUsage.objects.filter(server_id=serverid,timestamp__gte=start,timestamp__lte=end)
        return range_usages  

"""
Get CPU range with server_id the last five minitues
"""
class CpuUsageRealTimeList(generics.ListAPIView):
    lookup_field = "server_id"
    start = "start"
    end = "end"
    serializer_class = CpuUsageSerializer

    def get_queryset(self):
        serverid = self.kwargs.get(self.lookup_field)
        start = timezone.now() - timezone.timedelta(minutes=10)
        end = timezone.now()     
        range_usages = CpuUsage.objects.filter(server_id=serverid,timestamp__gte=start,timestamp__lte=end)
        return range_usages  