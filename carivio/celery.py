import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carivio.settings')

app = Celery('carivio')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()