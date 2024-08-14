import json
from datetime import datetime, timedelta

import requests
from celery.schedules import schedule
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from rest_framework import status

from config import settings


def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get(
        f'{settings.CUR_API_URL}/v3/latest?apikey={settings.CUR_API_KEY}&currencies=RUB'
    )
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = rub_price * usd_rate
        #print(response.json())
        # >>> {'meta': {'last_updated_at': '2024-08-11T23:59:59Z'}, 'data': {'RUB': {'code': 'RUB', 'value': 88.7374299952}}}

    return usd_price


# https://django-celery-beat.readthedocs.io/en/latest/
def set_scheduler(*args, **kwargs):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.HOURS,
    )
    PeriodicTask.objects.create(
        interval=schedule,  # we created this above.
        name='Importing contacts',  # simply describes this periodic task.
        task='proj.tasks.import_contacts',  # name of task.
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
