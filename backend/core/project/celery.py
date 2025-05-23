import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.project.settings')

app = Celery('core.project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(['core.apps.items'])

app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
