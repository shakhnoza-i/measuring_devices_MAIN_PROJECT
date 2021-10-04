#import python regex module
from collections import UserList
import re
from django.contrib import admin
from django.db import models
from django.core import validators
from django.contrib .auth.models import User
from django.contrib.gis.db.models import PointField
from uuid import UUID, uuid4
from django.contrib.auth.models import User



class Node(models.Model):   
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    geo = PointField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class City(Node):
    pass

class District(Node):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="districts")


class Street(Node):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="streets")


class House(Node):
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name="houses")


class Apartment(Node):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="apartments")



class Device(models.Model):
    uuid_deviсe = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    dev_eui = models.CharField(validators=[validators.MinLengthValidator(16)], max_length=16)
    activation_time = models.DateTimeField(auto_now_add=True)
    last_action_time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    description = models.CharField(max_length=255)
    deviсe_type = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="device")

    def __str__(self):
        return self.dev_eui


class Meter(models.Model):
    
    uuid_meter = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    serial_number = models.IntegerField()
    active = models.BooleanField(default=False)
    activation_time = models.DateTimeField(auto_now_add=True)
    first_action_time = models.DateTimeField(auto_now_add=True)
    initial_value = models.FloatField(default = 0)
    # charfield format is used yet, then necessary to create class with few options of physical units which is used by company
    unit = models.CharField(max_length=20) 
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="meter")
    # apartment = models.ForeignKey(Device, verbose_name = u'apartment', on_delete=models.CASCADE)
    # city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="district")

    def __str__(self):
        return self.unit

