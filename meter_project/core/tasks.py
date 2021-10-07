from __future__ import absolute_import, unicode_literals
from celery import shared_task
#from celery.task import task
from core.models import StatusCode
import requests



@shared_task
def response():
    url = 'https://www.google.kz/'
    r = requests.get(url)
    StatusCode.objects.create(code=r.status_code)
