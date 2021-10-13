#import python regex module
from collections import UserList
import re
from django.contrib import admin
from django.db import models
from django.core import validators
from django.contrib .auth.models import User
from django.contrib.gis.db.models import PointField
from django.contrib.postgres.fields import ArrayField
from uuid import UUID, uuid4
from django.contrib.auth.models import User
from accounts.models import Customer


class Node(models.Model):   
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    geo = PointField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, default=None)
    address = models.TextField(max_length=150)
    full_owner =  ArrayField(models.CharField(max_length=30, blank=True), blank=True, default=list)
    part_owner =  ArrayField(models.CharField(max_length=30, blank=True), blank=True, default=list)
    full_owner_link =  ArrayField(models.CharField(max_length=30, blank=True), blank=True, default=list)
    part_owner_link =  ArrayField(models.CharField(max_length=30, blank=True), blank=True, default=list)

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
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    dev_eui = models.CharField(validators=[validators.MinLengthValidator(16)], max_length=16)
    activation_time = models.DateTimeField(auto_now_add=True)
    last_action_time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=255)
    deviсe_type = models.CharField(max_length=30)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, default=None)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="devices")

    def __str__(self):
        return self.dev_eui


class Meter(models.Model):
    
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    serial_number = models.IntegerField()
    active = models.BooleanField(default=True)
    activation_time = models.DateTimeField(auto_now_add=True)
    first_action_time = models.DateTimeField(auto_now_add=True)
    initial_value = models.FloatField(default = 0)
    unit = models.CharField(max_length=20) 
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True,  default=None)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="meters")

    def __str__(self):
        return self.unit


class StatusCode(models.Model):
    code = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
