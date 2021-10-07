from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    description = models.CharField(max_length = 255)