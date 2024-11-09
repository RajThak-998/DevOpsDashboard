from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DevOpsDashboard.settings')

app = Celery('DevOpsDashboard')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'check-microservice-health-every-minute': {
        'task': 'monitoring.tasks.check_microservice_health',
        'schedule': crontab(minute='*/1'),
    },
}