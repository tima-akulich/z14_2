import time
from celery import shared_task
from datetime import timedelta

from celery.schedules import crontab
from django.core.mail import send_mail

from cooking.models import User
from cooking.parsers import VkusnoParser


@shared_task
def test_task():
    time.sleep(10)
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

@shared_task
def parse_site():
    parser = VkusnoParser()
    parser.parse()


SCHEDULE = {
    'send_test_mail': {
        'task': 'cooking.tasks.send_mails',
        'args': (),
        'options': {},
        'schedule': crontab()
    },

    'parse_site': {
        'task': 'cooking.tasks.parse_site',
        'args': (),
        'options': {},
        'schedule': crontab(minute=0, hour=0)
    }
}

