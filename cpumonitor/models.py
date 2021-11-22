from django.db import models

# Create your models here.
class CpuUsage(models.Model):
    server_id = models.IntegerField()
    sys_usage_percentage = models.FloatField()
    user_usage_percentage = models.FloatField()
    idle_usage_percentage = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f'{self.server_id}'

