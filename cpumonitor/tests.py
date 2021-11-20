from django.test import TestCase, Client

from cpumonitor.models import CpuUsage

class CpuUsageTestCase(TestCase):
    def setUp(self):
        CpuUsage.objects.create(server_id=1,sys_usage=0.2,user_usage=0.2,idle=0.2,created="")
        CpuUsage.objects.create(server_id=2,sys_usage=0.2,user_usage=0.2,idle=0.2,created="")

    def testGetRequest(self):
        client = Client()
        response = client.get('/cpu/1')
        self.assertEqual(response.status_code,200)

    def testGetListAllRequest(self):
        client = Client()
        response = client.get('/cpu/')
        self.assertEqual(response.status_code,200)

