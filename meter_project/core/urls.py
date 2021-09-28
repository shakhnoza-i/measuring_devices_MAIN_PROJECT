from django.urls import path, include
from core.views import (CityListGV, CityDetailGV, DistrictListGV, DistrictDetailGV,
                        StreetListGV, StreetDetailGV, HouseListGV, HouseDetailGV,
                        ApartmentListGV, ApartmentDetailGV,
                        DeviceListGV, DeviceDetailGV, MeterListGV, MeterDetailGV)


urlpatterns = [
    path('city/',  CityListGV.as_view(), name='city-list'),
    path('city/<int:pk>/',  CityDetailGV.as_view(), name='city-details'),
    
    path('district/',  DistrictListGV.as_view(), name='district-list'),
    path('district/<int:pk>/',  DistrictDetailGV.as_view(), name='district-details'),

    path('street/',  StreetListGV.as_view(), name='street-list'),
    path('street/<int:pk>/',  StreetDetailGV.as_view(), name='street-details'),

    path('house/',  HouseListGV.as_view(), name='house-list'),
    path('house/<int:pk>/',  HouseDetailGV.as_view(), name='house-details'),

    path('apartment/',  ApartmentListGV.as_view(), name='apartment-list'),
    path('apartment/<int:pk>/',  ApartmentDetailGV.as_view(), name='apartment-details'),

    path('device/',  DeviceListGV.as_view(), name='device-list'),
    path('device/<int:pk>/',  DeviceDetailGV.as_view(), name='device-details'),
    
    path('meter/',  MeterListGV.as_view(), name='meter-list'),
    path('meter/<int:pk>/',  MeterDetailGV.as_view(), name='meter-details'),
]