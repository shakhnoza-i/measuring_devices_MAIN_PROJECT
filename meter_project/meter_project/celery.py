from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from rest_framework import status
from rest_framework.response import Response



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meter_project.settings")

app = Celery("meter_project")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

