from core.models import City, District, Street, House, Apartment, Device, Meter
from core.serializers import (CitySerializer, DistrictSerializer, 
                              StreetSerializer, HouseSerializer, ApartmentSerializer, 
                              DeviceSerializer, MeterSerializer)

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CityListGV(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailGV(generics.RetrieveUpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer



class DistrictListGV(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class DistrictDetailGV(generics.RetrieveUpdateAPIView):
    queryset = City.objects.all()
    serializer_class = DistrictSerializer



class StreetListGV(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StreetDetailGV(generics.RetrieveUpdateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer



class HouseListGV(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseDetailGV(generics.RetrieveUpdateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer



class ApartmentListGV(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class ApartmentDetailGV(generics.RetrieveUpdateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer



class DeviceListGV(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer



class MeterListGV(generics.ListCreateAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer


class MeterDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = MeterSerializer


