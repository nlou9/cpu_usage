from datetime import datetime
from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from django.utils import timezone

# Get an instance of a logger
logger = logging.getLogger(__name__)

class CpumonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cpumonitor'
    
    def ready(self): 
        print("start poll CPU status in every 10s")
        from .task import Task   
        try:   
            scheduler = BackgroundScheduler(timezone='UTC')
            scheduler.add_job(Task(1).update_database,'interval',seconds=15)
            scheduler.start()
        except Exception as e:
            logger.error(e)
            pass

        
 
        
        
        
        

