from django.db import models
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
    locate = models.ForeignKey(City,on_delete=models.CASCADE,related_name="city")

    def __str__(self):
        return self.name


class Street(models.Model):
    uuid_street = models.UUIDField(format='hex_verbose')
    geo = PointField()
    name = models.CharField(min_length=3, max_length=30)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=30)
    address = models.TextField(min_length=3, max_length=150)
    locate = models.ForeignKey(District,on_delete=models.CASCADE,related_name="district")

    def __str__(self):
        return self.name


class House(models.Model):
    uuid_house = models.UUIDField(format='hex_verbose')
    geo = PointField()
    name = models.CharField(min_length=3, max_length=30)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=30)
    address = models.TextField(min_length=3, max_length=150)
    locate = models.ForeignKey(Street,on_delete=models.CASCADE,related_name="street")

    def __str__(self):
        return self.name


class Apartment(models.Model):
    uuid_apartment = models.UUIDField(format='hex_verbose')
    geo = PointField()
    name = models.CharField(min_length=3, max_length=30)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=30)
    address = models.TextField(min_length=3, max_length=150)
    locate = models.ForeignKey(House,on_delete=models.CASCADE,related_name="house")

    def __str__(self):
        return self.name


# class Devise:
#     uuid_devise = models.UUIDField(format='hex_verbose')
#     dev_eui = 