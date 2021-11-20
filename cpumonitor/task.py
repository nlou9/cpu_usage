import datetime
from .models import CpuUsage
import subprocess

"""
Schedule a task update_database to poll CPU usage information and insert into database
"""

class Task:
    def __init__(self,server_id = 1):
        self.server_id = server_id

    def update_database(self):
        cmd = "top -l 1 | awk '/CPU usage:/ {print $3,$5,$7}'"
        load = subprocess.check_output(cmd, shell = True ).decode("utf-8").strip().split(" ")
        load_list = [float(x.strip("%")) for x in load]

        cpu_realtime_usage = CpuUsage(
            server_id=self.server_id,
            sys_usage=load_list[0],
            user_usage=load_list[1],
            idle=load_list[2],
            created= "",
            )
        cpu_realtime_usage.save()  