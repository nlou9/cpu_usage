from django.db import models

# Create your models here.
class CpuUsage(models.Model):
    server_id = models.IntegerField()
    sys_usage = models.FloatField()
    user_usage = models.FloatField()
    idle = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

