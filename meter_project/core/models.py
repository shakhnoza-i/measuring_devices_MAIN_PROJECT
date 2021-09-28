#import python regex module
import re
from django.db import models
from django.core import validators
from django.contrib .auth.models import User
from django.contrib.gis.db.models import PointField
from uuid import UUID, uuid4


class City(models.Model):
    uuid_city = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    geo = PointField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=150)

    def __str__(self):
        return self.name


class District(models.Model):
    uuid_district = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    geo = PointField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="district")

    def __str__(self):
        return self.name


class Street(models.Model):
    uuid_street = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    geo = PointField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=150)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="street")

    def __str__(self):
        return self.name


class House(models.Model):
    uuid_house = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    geo = PointField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=150)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name="house")

    def __str__(self):
        return self.name


class Apartment(models.Model):
    uuid_apartment = models.UUIDField(unique=True, default=uuid4, editable=False, db_index=True)
    geo = PointField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=150)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="apartment")

    def __str__(self):
        return self.name


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
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit
