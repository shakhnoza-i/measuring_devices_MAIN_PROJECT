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
                              DeviceDateTimeRangeSerializer, MeterSerializer, 
                              MeterUUIDSerializer, DeviceUUIDSerializer, ApartmentUUIDSerializer, 
                              HouseUUIDSerializer, StreetUUIDSerializer, DistrictUUIDSerializer,
                              CityUUIDSerializer)


class CityListGV(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.user.username
        return City.objects.filter(owner__username=username)


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
            new_full_owner = Customer.objects.get(username=request.query_params.get('full_owner'))
            a = str(new_full_owner) + request.user.username
            city.full_owner.append(new_full_owner)
            city.full_owner_link.append(a)
            city.save()
            return HttpResponse("You've added the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('part_owner') is not None:
            new_part_owner = Customer.objects.get(username=request.query_params.get('part_owner'))
            b = str(new_part_owner) + request.user.username
            city.part_owner.append(new_part_owner)
            city.part_owner_link.append(b)
            city.save()
            return HttpResponse("You've added the part access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_full_owner') is not None:
            remove_full_owner = Customer.objects.get(username=request.query_params.get('remove_full_owner'))
            a = str(remove_full_owner) + request.user.username
            full_owner_links=city.full_owner_link
            if full_owner_links is not None:
                for i in full_owner_links:
                    if i == a:
                        city.full_owner.remove(str(remove_full_owner))
                        #city.full_owner.remove(remove_full_owner)
                        city.full_owner_link.remove(a)
                        city.save()
                        return HttpResponse("You've removed the full access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_part_owner') is not None:
            remove_part_owner = Customer.objects.get(username=request.query_params.get('remove_part_owner'))
            a = str(remove_part_owner) + request.user.username
            part_owner_links=city.part_owner_link
            if part_owner_links is not None:
                for i in part_owner_links:
                    if i == a:
                        city.part_owner.remove(str(remove_part_owner))
                        city.part_owner_link.remove(a)
                        city.save()
                        return HttpResponse("You've removed the part access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the part access for this user", status=status.HTTP_200_OK)
        else:
            return HttpResponse(city, status=status.HTTP_200_OK)


class DistrictListGV(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.user.username
        return District.objects.filter(owner__username=username)


class DistrictDetailGV(generics.RetrieveUpdateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [IsCustomer]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        node = District.objects.get(pk=pk)
        #owner_link = city.owner_link.all()
        if request.query_params.get('full_owner') is not None:
            new_full_owner = Customer.objects.get(username=request.query_params.get('full_owner'))
            a = str(new_full_owner) + request.user.username
            node.full_owner.append(new_full_owner)
            node.full_owner_link.append(a)
            node.save()
            return HttpResponse("You've added the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('part_owner') is not None:
            new_part_owner = Customer.objects.get(username=request.query_params.get('part_owner'))
            b = str(new_part_owner) + request.user.username
            node.part_owner.append(new_part_owner)
            node.part_owner_link.append(b)
            node.save()
            return HttpResponse("You've added the part access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_full_owner') is not None:
            remove_full_owner = Customer.objects.get(username=request.query_params.get('remove_full_owner'))
            a = str(remove_full_owner) + request.user.username
            full_owner_links=node.full_owner_link
            if full_owner_links is not None:
                for i in full_owner_links:
                    if i == a:
                        node.full_owner.remove(str(remove_full_owner))
                        #city.full_owner.remove(remove_full_owner)
                        node.full_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the full access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_part_owner') is not None:
            remove_part_owner = Customer.objects.get(username=request.query_params.get('remove_part_owner'))
            a = str(remove_part_owner) + request.user.username
            part_owner_links=node.part_owner_link
            if part_owner_links is not None:
                for i in part_owner_links:
                    if i == a:
                        node.part_owner.remove(str(remove_part_owner))
                        node.part_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the part access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the part access for this user", status=status.HTTP_200_OK)
        else:
            return HttpResponse(node, status=status.HTTP_200_OK)


class StreetListGV(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.user.username
        return Street.objects.filter(owner__username=username)


class StreetDetailGV(generics.RetrieveUpdateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = [IsCustomer]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        node = Street.objects.get(pk=pk)
        #owner_link = city.owner_link.all()
        if request.query_params.get('full_owner') is not None:
            new_full_owner = Customer.objects.get(username=request.query_params.get('full_owner'))
            a = str(new_full_owner) + request.user.username
            node.full_owner.append(new_full_owner)
            node.full_owner_link.append(a)
            node.save()
            return HttpResponse("You've added the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('part_owner') is not None:
            new_part_owner = Customer.objects.get(username=request.query_params.get('part_owner'))
            b = str(new_part_owner) + request.user.username
            node.part_owner.append(new_part_owner)
            node.part_owner_link.append(b)
            node.save()
            return HttpResponse("You've added the part access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_full_owner') is not None:
            remove_full_owner = Customer.objects.get(username=request.query_params.get('remove_full_owner'))
            a = str(remove_full_owner) + request.user.username
            full_owner_links=node.full_owner_link
            if full_owner_links is not None:
                for i in full_owner_links:
                    if i == a:
                        node.full_owner.remove(str(remove_full_owner))
                        #city.full_owner.remove(remove_full_owner)
                        node.full_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the full access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_part_owner') is not None:
            remove_part_owner = Customer.objects.get(username=request.query_params.get('remove_part_owner'))
            a = str(remove_part_owner) + request.user.username
            part_owner_links=node.part_owner_link
            if part_owner_links is not None:
                for i in part_owner_links:
                    if i == a:
                        node.part_owner.remove(str(remove_part_owner))
                        node.part_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the part access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the part access for this user", status=status.HTTP_200_OK)
        else:
            return HttpResponse(node, status=status.HTTP_200_OK)



class HouseListGV(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.user.username
        return House.objects.filter(owner__username=username)


class HouseDetailGV(generics.RetrieveUpdateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsCustomer]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        node = House.objects.get(pk=pk)
        #owner_link = city.owner_link.all()
        if request.query_params.get('full_owner') is not None:
            new_full_owner = Customer.objects.get(username=request.query_params.get('full_owner'))
            a = str(new_full_owner) + request.user.username
            node.full_owner.append(new_full_owner)
            node.full_owner_link.append(a)
            node.save()
            return HttpResponse("You've added the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('part_owner') is not None:
            new_part_owner = Customer.objects.get(username=request.query_params.get('part_owner'))
            b = str(new_part_owner) + request.user.username
            node.part_owner.append(new_part_owner)
            node.part_owner_link.append(b)
            node.save()
            return HttpResponse("You've added the part access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_full_owner') is not None:
            remove_full_owner = Customer.objects.get(username=request.query_params.get('remove_full_owner'))
            a = str(remove_full_owner) + request.user.username
            full_owner_links=node.full_owner_link
            if full_owner_links is not None:
                for i in full_owner_links:
                    if i == a:
                        node.full_owner.remove(str(remove_full_owner))
                        #city.full_owner.remove(remove_full_owner)
                        node.full_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the full access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_part_owner') is not None:
            remove_part_owner = Customer.objects.get(username=request.query_params.get('remove_part_owner'))
            a = str(remove_part_owner) + request.user.username
            part_owner_links=node.part_owner_link
            if part_owner_links is not None:
                for i in part_owner_links:
                    if i == a:
                        node.part_owner.remove(str(remove_part_owner))
                        node.part_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the part access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the part access for this user", status=status.HTTP_200_OK)
        else:
            return HttpResponse(node, status=status.HTTP_200_OK)



class ApartmentListGV(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'address', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.user.username
        return Apartment.objects.filter(owner__username=username)


class ApartmentDetailGV(generics.RetrieveUpdateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsCustomer]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        node = Apartment.objects.get(pk=pk)
        #owner_link = city.owner_link.all()
        if request.query_params.get('full_owner') is not None:
            new_full_owner = Customer.objects.get(username=request.query_params.get('full_owner'))
            a = str(new_full_owner) + request.user.username
            node.full_owner.append(new_full_owner)
            node.full_owner_link.append(a)
            node.save()
            return HttpResponse("You've added the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('part_owner') is not None:
            new_part_owner = Customer.objects.get(username=request.query_params.get('part_owner'))
            b = str(new_part_owner) + request.user.username
            node.part_owner.append(new_part_owner)
            node.part_owner_link.append(b)
            node.save()
            return HttpResponse("You've added the part access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_full_owner') is not None:
            remove_full_owner = Customer.objects.get(username=request.query_params.get('remove_full_owner'))
            a = str(remove_full_owner) + request.user.username
            full_owner_links=node.full_owner_link
            if full_owner_links is not None:
                for i in full_owner_links:
                    if i == a:
                        node.full_owner.remove(str(remove_full_owner))
                        #city.full_owner.remove(remove_full_owner)
                        node.full_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the full access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_part_owner') is not None:
            remove_part_owner = Customer.objects.get(username=request.query_params.get('remove_part_owner'))
            a = str(remove_part_owner) + request.user.username
            part_owner_links=node.part_owner_link
            if part_owner_links is not None:
                for i in part_owner_links:
                    if i == a:
                        node.part_owner.remove(str(remove_part_owner))
                        node.part_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the part access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the part access for this user", status=status.HTTP_200_OK)
        else:
            return HttpResponse(node, status=status.HTTP_200_OK)



class DeviceListGV(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dev_eui', 'owner', 'uuid']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.user.username
        return Device.objects.filter(owner__username=username)


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

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        node = Device.objects.get(pk=pk)
        #owner_link = city.owner_link.all()
        if request.query_params.get('full_owner') is not None:
            new_full_owner = Customer.objects.get(username=request.query_params.get('full_owner'))
            a = str(new_full_owner) + request.user.username
            node.full_owner.append(new_full_owner)
            node.full_owner_link.append(a)
            node.save()
            return HttpResponse("You've added the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('part_owner') is not None:
            new_part_owner = Customer.objects.get(username=request.query_params.get('part_owner'))
            b = str(new_part_owner) + request.user.username
            node.part_owner.append(new_part_owner)
            node.part_owner_link.append(b)
            node.save()
            return HttpResponse("You've added the part access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_full_owner') is not None:
            remove_full_owner = Customer.objects.get(username=request.query_params.get('remove_full_owner'))
            a = str(remove_full_owner) + request.user.username
            full_owner_links=node.full_owner_link
            if full_owner_links is not None:
                for i in full_owner_links:
                    if i == a:
                        node.full_owner.remove(str(remove_full_owner))
                        #city.full_owner.remove(remove_full_owner)
                        node.full_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the full access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_part_owner') is not None:
            remove_part_owner = Customer.objects.get(username=request.query_params.get('remove_part_owner'))
            a = str(remove_part_owner) + request.user.username
            part_owner_links=node.part_owner_link
            if part_owner_links is not None:
                for i in part_owner_links:
                    if i == a:
                        node.part_owner.remove(str(remove_part_owner))
                        node.part_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the part access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the part access for this user", status=status.HTTP_200_OK)
        else:
            return HttpResponse(node, status=status.HTTP_200_OK)



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

    def get_queryset(self):
        username = self.request.user.username
        return Meter.objects.filter(owner__username=username)


class MeterDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer
    permission_classes = [IsCustomer] 
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        node = Meter.objects.get(pk=pk)
        #owner_link = city.owner_link.all()
        if request.query_params.get('full_owner') is not None:
            new_full_owner = Customer.objects.get(username=request.query_params.get('full_owner'))
            a = str(new_full_owner) + request.user.username
            node.full_owner.append(new_full_owner)
            node.full_owner_link.append(a)
            node.save()
            return HttpResponse("You've added the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('part_owner') is not None:
            new_part_owner = Customer.objects.get(username=request.query_params.get('part_owner'))
            b = str(new_part_owner) + request.user.username
            node.part_owner.append(new_part_owner)
            node.part_owner_link.append(b)
            node.save()
            return HttpResponse("You've added the part access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_full_owner') is not None:
            remove_full_owner = Customer.objects.get(username=request.query_params.get('remove_full_owner'))
            a = str(remove_full_owner) + request.user.username
            full_owner_links=node.full_owner_link
            if full_owner_links is not None:
                for i in full_owner_links:
                    if i == a:
                        node.full_owner.remove(str(remove_full_owner))
                        #city.full_owner.remove(remove_full_owner)
                        node.full_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the full access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the full access for this user", status=status.HTTP_200_OK)
        elif request.query_params.get('remove_part_owner') is not None:
            remove_part_owner = Customer.objects.get(username=request.query_params.get('remove_part_owner'))
            a = str(remove_part_owner) + request.user.username
            part_owner_links=node.part_owner_link
            if part_owner_links is not None:
                for i in part_owner_links:
                    if i == a:
                        node.part_owner.remove(str(remove_part_owner))
                        node.part_owner_link.remove(a)
                        node.save()
                        return HttpResponse("You've removed the part access for this user", status=status.HTTP_200_OK)
                    else:
                        return HttpResponse("You can't remove the part access for this user", status=status.HTTP_200_OK)
        else:
            return HttpResponse(node, status=status.HTTP_200_OK)



class CityUUIDListGV(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityUUIDSerializer


class CityUUIDDetailGV(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityUUIDSerializer
  

class DistrictUUIDListGV(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictUUIDSerializer
 

class DistrictUUIDDetailGV(generics.RetrieveAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictUUIDSerializer


class StreetUUIDListGV(generics.ListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetUUIDSerializer


class StreetUUIDDetailGV(generics.RetrieveAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetUUIDSerializer


class HouseUUIDListGV(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseUUIDSerializer


class HouseUUIDDetailGV(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseUUIDSerializer


class ApartmentUUIDListGV(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentUUIDSerializer


class ApartmentUUIDDetailGV(generics.RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentUUIDSerializer


class DeviceUUIDListGV(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceUUIDSerializer


class DeviceUUIDDetailGV(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceUUIDSerializer


class MeterUUIDListGV(generics.ListAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterUUIDSerializer


class MeterUUIDDetailGV(generics.RetrieveAPIView):
    queryset = Meter.objects.all()
    serializer_class = MeterUUIDSerializer
