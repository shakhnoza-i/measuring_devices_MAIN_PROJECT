from __future__ import unicode_literals
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db import models, migrations
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http.response import HttpResponse
from django.apps import apps
from django.http import FileResponse
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
import datetime

from accounts.models import Customer
from core.permissions import IsCustomer
from core.models import Node, City, District, Street, House, Apartment, Device, Meter
from core.serializers import (CitySerializer, DistrictSerializer, StreetSerializer, 
                              HouseSerializer, ApartmentSerializer, DeviceSerializer, 
                              DeviceDateTimeRangeSerializer, MeterSerializer)


class CityListGV(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     username = self.request.query_params.get('username')
    #     return City.objects.filter(owner__username=username)


class CityDetailGV(generics.RetrieveUpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    #transfer of full rights
    permission_classes = [IsCustomer]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        city = City.objects.get(pk=pk)
        #owner_link = city.owner_link.all()
        if request.query_params.get('full_owner') is not None:
            add_full_owner = Customer.objects.get(username=request.query_params.get('full_owner'))
            #a = new_full_owner + request.user.username
            city.full_owner = city.full_owner.append(add_full_owner)
            #city.owner_link = city.owner_link.add(a)
            city.save()
            return HttpResponse(city, status=status.HTTP_200_OK)
        elif request.query_params.get('part_owner') is not None:
            add_part_owner = Customer.objects.get(username=request.query_params.get('part_owner'))
            city.part_owner = city.part_owner.append(add_part_owner)
            city.save()
            return HttpResponse(city, status=status.HTTP_200_OK)


class DistrictListGV(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]


class DistrictDetailGV(generics.RetrieveUpdateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [IsCustomer]


class StreetListGV(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]


class StreetDetailGV(generics.RetrieveUpdateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = [IsCustomer]


class HouseListGV(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]


class HouseDetailGV(generics.RetrieveUpdateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsCustomer]


class ApartmentListGV(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]


class ApartmentDetailGV(generics.RetrieveUpdateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsCustomer]


class DeviceListGV(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dev_eui', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]


class DeviceDateTimeRangeGV(generics.ListAPIView):
    serializer_class = DeviceDateTimeRangeSerializer

    #period = Device.objects.filter(date__range=["2011-01-01", "2011-01-31"])
    def get_queryset(self, request):
        queryset = Device.objects.all()
        start_date = datetime(self.request.query_params.get('start_date', ''))
        end_date = datetime(self.request.query_params.get('end_date', ''))
        last_action_time = Device.objects.get('last_action_time')
      
        if last_action_time is not None:
            queryset = queryset.filter(last_action_time=[start_date, end_date])
        return queryset


class DeviceDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsCustomer]


class PassthroughRenderer(renderers.BaseRenderer):
    """
        Return data as-is. View should supply a Response.
    """
    media_type = 'text/csv'
    format = 'csv'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data


class DeviceDetailDownloadGV(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    renderer_classes=(PassthroughRenderer,)
    permission_classes = [IsCustomer]

    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response
    

class MeterListGV(generics.ListCreateAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['serial_number', 'uuid']
    permission_classes = [IsAuthenticated]


class MeterDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer
    permission_classes = [IsCustomer] 
