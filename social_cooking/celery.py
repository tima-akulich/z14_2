import os
import django

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_cooking.settings')
django.setup()

from cooking.tasks import SCHEDULE as COOKING_SCHEDULE

app = Celery('social_cooking')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = COOKING_SCHEDULE
app.autodiscover_tasks()
