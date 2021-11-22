import datetime
from .models import CpuUsage
import subprocess
import logging

"""
Schedule a task update_database to poll CPU usage information in Linux System and insert into database
"""
# Get an instance of a logger
logger = logging.getLogger(__name__)

class Task:
    def __init__(self,server_id = 1):
        self.server_id = server_id

    def update_database(self):
        cmd = "top -l 1 | awk '/CPU usage:/ {print $3,$5,$7}'"
        load = subprocess.check_output(cmd, shell = True ).decode("utf-8").strip().split(" ")
        load_list = [float(x.strip("%")) for x in load]
        if load_list:          
            cpu_realtime_usage = CpuUsage(
                server_id=self.server_id,
                sys_usage_percentage=load_list[0],
                user_usage_percentage=load_list[1],
                idle_usage_percentage=load_list[2],
                timestamp= "",
                )
            cpu_realtime_usage.save() 
        else:
            logger.info("top -l 1 return empty information") 