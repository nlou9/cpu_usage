from django.urls import path
from . import views

"""
Router to redirect to views
"""

urlpatterns = [
    path("cpu/",views.CpuUsageCreate.as_view()),
    path('cpu/<int:server_id>', views.CpuUsageList.as_view(), name='cpu-detail'),
    path('cpu/<int:server_id>/<start>/<end>', views.CpuUsageTimeRangeList.as_view(), name='cpu-detail'),
    path('cpu/<int:server_id>/realtime', views.CpuUsageRealTimeList.as_view(), name='cpu-detail'),
    ]
