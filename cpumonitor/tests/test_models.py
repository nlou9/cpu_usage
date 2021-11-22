from django.test import TestCase

from cpumonitor.models import CpuUsage

class CpuModelsTest(TestCase):

    def create_cpu_obj(self,server_id=1, sys_usage_percentage=10,user_usage_percentage=20,idle_usage_percentage=30,timestamp=""):
        # Set up non-modified objects used by all test methods
        return CpuUsage.objects.create(server_id=server_id, sys_usage_percentage=sys_usage_percentage,user_usage_percentage=user_usage_percentage,idle_usage_percentage=idle_usage_percentage,timestamp=timestamp)

    def test_create(self):
        obj = self.create_cpu_obj()
        self.assertTrue(isinstance(obj,CpuUsage))
