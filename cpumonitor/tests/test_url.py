from django.test import TestCase, Client
from cpumonitor.models import CpuUsage
import unittest
from django.core.exceptions import ValidationError

class CpuUsageTestCase(unittest.TestCase):
   
    def test_get_cpu_by_serverid(self):
        client = Client()
        response = client.get('/cpu/1')
        #Check that the reponse is 200 OK
        self.assertEqual(response.status_code,200)

    def test_get_cpu(self):
        client = Client()
        response = client.get('/cpu/')
        #Check that the reponse is 200 OK
        self.assertEqual(response.status_code,200)

    def test_get_cpu_time_range(self):
        client = Client()
        response = client.get('/cpu/1/2021-11-21T00:06:01.909068Z/2021-11-22T00:06:01.909068Z')
        self.assertEqual(response.status_code,200)

    def test_get_cpu(self):
        client = Client()
        response = client.get('/cpu/1/realtime')
        #Check that the reponse is 200 OK
        self.assertEqual(response.status_code,200)

    def test_get_cpu_return_404(self):
        client = Client()
        response = client.get('/cpu/a')
        #Check that the reponse is 404
        self.assertEqual(response.status_code,404) 

    @unittest.expectedFailure
    def test_get_cpu_time_range_exception(self):
        client = Client()
        response = client.get('/cpu/1/2021-11-20/2021-11-21')   
      
    @unittest.expectedFailure
    def test_get_cpu_time_invalid_exception(self):
        client = Client()
        #end is early than begin
        response = client.get('/cpu/1/2021-11-22T00:06:01.909068Z/2021-11-21T00:06:01.909068Z')  
    