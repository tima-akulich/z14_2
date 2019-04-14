
import time
from celery import shared_task
from datetime import timedelta

from celery.schedules import crontab
from celery.task import periodic_task
from django.core.mail import send_mail

from cooking.models import User
from cooking.utils import parsing_site


@shared_task
def test_task():
    time.sleep(3)
    print('qwee')
    return 1


@shared_task
def test_sum(arg1, arg2):
    time.sleep(3)
    return arg1 + arg2


@shared_task
def send_mails():
    emails = User.objects.all().values_list('email', flat=True)
    send_mail('Test mail', 'Some message', 'admin@cooking.io', emails)
    print('Here')


SCHEDULE = {
    'send_test_mail': {
        'task': 'cooking.tasks.send_mails',
        'args': (),
        'options': {},
        'schedule': crontab()
    }
}


@periodic_task(run_every=crontab(hour=0, minute=0))
def parsing_site_task():
    parsing_site()
