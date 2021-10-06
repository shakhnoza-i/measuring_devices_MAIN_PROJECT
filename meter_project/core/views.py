from __future__ import unicode_literals

from django.http.response import HttpResponse
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
from django.db import models, migrations

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.apps import apps

from accounts.models import Customer


class CityListGV(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']


class CityDetailGV(generics.RetrieveUpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def patch(self, request, *args, **kwargs):   
        if request.query_params.get('owner') is not None:
            owner = Customer.objects.get(username=request.query_params.get('owner'))
            model = apps.get_model(app_label='core', model_name='city')

            content_type = ContentType.objects.get_for_model(model)
            all_permissions = Permission.objects.filter(content_type=content_type)

            print (all_permissions)
            for i in all_permissions:
                owner.user_permissions.add(i)
                owner.save()
            return HttpResponse('Success')
            #return HttpResponse(owner.save())

        return super().patch(request, *args, **kwargs)


class DistrictListGV(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']


class DistrictDetailGV(generics.RetrieveUpdateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def patch(self, request, *args, **kwargs):   
        if request.query_params.get('owner') is not None:
            owner = Customer.objects.get(username=request.query_params.get('owner'))
            model = apps.get_model(app_label='core', model_name='district')

            content_type = ContentType.objects.get_for_model(model)
            all_permissions = Permission.objects.filter(content_type=content_type)

            # print (all_permissions)
            for i in all_permissions:
                owner.user_permissions.add(i)
            return HttpResponse('Success')

        return super().patch(request, *args, **kwargs)


class StreetListGV(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']


class StreetDetailGV(generics.RetrieveUpdateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def patch(self, request, *args, **kwargs):   
        if request.query_params.get('owner') is not None:
            owner = Customer.objects.get(username=request.query_params.get('owner'))
            model = apps.get_model(app_label='core', model_name='street')

            content_type = ContentType.objects.get_for_model(model)
            all_permissions = Permission.objects.filter(content_type=content_type)

            # print (all_permissions)
            for i in all_permissions:
                owner.user_permissions.add(i)
            return HttpResponse('Success')

        return super().patch(request, *args, **kwargs)


class HouseListGV(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']


class HouseDetailGV(generics.RetrieveUpdateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def patch(self, request, *args, **kwargs):   
        if request.query_params.get('owner') is not None:
            owner = Customer.objects.get(username=request.query_params.get('owner'))
            model = apps.get_model(app_label='core', model_name='house')

            content_type = ContentType.objects.get_for_model(model)
            all_permissions = Permission.objects.filter(content_type=content_type)

            # print (all_permissions)
            for i in all_permissions:
                owner.user_permissions.add(i)
            return HttpResponse('Success')

        return super().patch(request, *args, **kwargs)


class ApartmentListGV(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']


class ApartmentDetailGV(generics.RetrieveUpdateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    def patch(self, request, *args, **kwargs):   
        if request.query_params.get('owner') is not None:
            owner = Customer.objects.get(username=request.query_params.get('owner'))
            model = apps.get_model(app_label='core', model_name='apartment')

            content_type = ContentType.objects.get_for_model(model)
            all_permissions = Permission.objects.filter(content_type=content_type)

            # print (all_permissions)
            for i in all_permissions:
                owner.user_permissions.add(i)
            return HttpResponse('Success')

        return super().patch(request, *args, **kwargs)


class DeviceListGV(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dev_eui', 'owner', 'uuid']

    #period = Device.objects.filter(date__range=["2011-01-01", "2011-01-31"])
    def get_queryset(self):
        start_date = models.DateTimeField()
        end_date = models.DateTimeField()
        #books = Device.objects.filter(last_action_time=(start_date, end_date))
        queryset = Device.objects.all()
        last_action_time = self.request.query_params.get('last_action_time')
        if last_action_time is not None:
            queryset = queryset.filter(last_action_time=(start_date, end_date))
        return queryset


class DeviceDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def patch(self, request, *args, **kwargs):   
        if request.query_params.get('owner') is not None:
            owner = Customer.objects.get(username=request.query_params.get('owner'))
            model = apps.get_model(app_label='core', model_name='device')

            content_type = ContentType.objects.get_for_model(model)
            all_permissions = Permission.objects.filter(content_type=content_type)

            # print (all_permissions)
            for i in all_permissions:
                owner.user_permissions.add(i)
            return HttpResponse('Success')

        return super().patch(request, *args, **kwargs)


class MeterListGV(generics.ListCreateAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['serial_number', 'uuid']


class MeterDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer

    def patch(self, request, *args, **kwargs):   
        if request.query_params.get('owner') is not None:
            owner = Customer.objects.get(username=request.query_params.get('owner'))
            model = apps.get_model(app_label='core', model_name='meter')

            content_type = ContentType.objects.get_for_model(model)
            all_permissions = Permission.objects.filter(content_type=content_type)

            # print (all_permissions)
            for i in all_permissions:
                owner.user_permissions.add(i)
            return HttpResponse('Success')

        return super().patch(request, *args, **kwargs)  