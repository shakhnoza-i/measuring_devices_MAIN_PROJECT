from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib .auth.models import User
from django.contrib.gis.db.models import PointField


class City(models.Model):
    uuid_city = models.UUIDField(format='hex_verbose')
    geo = PointField()
    name = models.CharField(min_length=3, max_length=30)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=30)
    address = models.TextField(min_length=3, max_length=150)

    def __str__(self):
        return self.name


class District(models.Model):
    uuid_district = models.UUIDField(format='hex_verbose')
    geo = PointField()
    name = models.CharField(min_length=3, max_length=30)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=30)
    address = models.TextField(min_length=3, max_length=150)
    locate = models.ForeignKey(City, on_delete=models.CASCADE, related_name="district")

    def __str__(self):
        return self.name


class Street(models.Model):
    uuid_street = models.UUIDField(format='hex_verbose')
    geo = PointField()
    name = models.CharField(min_length=3, max_length=30)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=30)
    address = models.TextField(min_length=3, max_length=150)
    locate = models.ForeignKey(City or District, on_delete=models.CASCADE, related_name="street")

    def __str__(self):
        return self.name


class House(models.Model):
    uuid_house = models.UUIDField(format='hex_verbose')
    geo = PointField()
    name = models.CharField(min_length=3, max_length=30)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=30)
    address = models.TextField(min_length=3, max_length=150)
    locate = models.ForeignKey(Street, on_delete=models.CASCADE, related_name="house")

    def __str__(self):
        return self.name


class Apartment(models.Model):
    uuid_apartment = models.UUIDField(format='hex_verbose')
    geo = PointField()
    name = models.CharField(min_length=3, max_length=30)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=30)
    address = models.TextField(min_length=3, max_length=150)
    locate = models.ForeignKey(House, on_delete=models.CASCADE, related_name="apartment")

    def __str__(self):
        return self.name


class Device(models.Model):
    uuid_devise = models.UUIDField(format='hex_verbose')
    dev_eui = models.IPAddressField(protocol='ipv6') # EUI-64 format is also used in IpAddressing
    activation_time = models.DateTimeField(auto_now_add=True)
    last_action_time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    description = models.CharField(min_length=3, max_length=255)
    devise_type = models.CharField(min_length=3, max_length=30)
    owner = models.CharField(min_length=3, max_length=30)
    locate = models.ForeignKey(House or Apartment, on_delete=models.CASCADE, related_name="device")

    def __str__(self):
        return self.dev_eui


class Meter(models.Model):
    uuid_devise = models.UUIDField(format='hex_verbose')
    serial_number = models.IntegerField(max_value=None, min_value=0)
    active = models.BooleanField(default=False)
    activation_time = models.DateTimeField(auto_now_add=True)
    first_action_time = models.DateTimeField(auto_now_add=True)
    initial_value = models.FloatField(max_value=None, min_value=0, default = 0)
    # charfield format is used yet, then necessary to create class with few options of physical units which is used by company
    unit = models.CharField(min_length=1, max_length=10) 
    locate = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="meter")

    def __str__(self):
        return self.serial_number
