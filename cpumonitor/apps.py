from datetime import datetime
from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler

class CpumonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cpumonitor'
    
    def ready(self): 
        print("start poll CPU status in every 10s")
        from .task import Task      
        scheduler = BackgroundScheduler()
        scheduler.add_job(Task(1).update_database,'interval',seconds=15)
        scheduler.start()
        
 
        
        
        
        

