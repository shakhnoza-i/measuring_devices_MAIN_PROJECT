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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid_city']



class CityDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer



class DistrictListGV(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid_district']


class DistrictDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer



class StreetListGV(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid_street']


class StreetDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer



class HouseListGV(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid_house']


class HouseDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer



class ApartmentListGV(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid_apartment']


class ApartmentDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer



class DeviceListGV(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dev_eui', 'owner', 'uuid_deviсe']

class DeviceDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer



class MeterListGV(generics.ListCreateAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['serial_number', 'uuid_meter']


class MeterDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer


