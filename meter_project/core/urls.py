from django.urls import path, include
from core.views import (CityListGV, CityDetailGV, DistrictListGV, DistrictDetailGV,
                        StreetListGV, StreetDetailGV, HouseListGV, HouseDetailGV,
                        ApartmentListGV, ApartmentDetailGV, DeviceListGV, DeviceDateTimeRangeGV,
                        DeviceDetailGV, DeviceDetailDownloadGV, MeterListGV, MeterDetailGV,

                        CityUUIDListGV, CityUUIDDetailGV, DistrictUUIDListGV, DistrictUUIDDetailGV,
                        StreetUUIDListGV, StreetUUIDDetailGV, HouseUUIDListGV, HouseUUIDDetailGV,
                        ApartmentUUIDListGV, ApartmentUUIDDetailGV, DeviceUUIDListGV,
                        DeviceUUIDDetailGV, MeterUUIDListGV, MeterUUIDDetailGV)


urlpatterns = [
    path('city/',  CityListGV.as_view(), name='city-list'),
    path('city/<int:pk>/',  CityDetailGV.as_view(), name='city-details'),
    path('city_uuid/',  CityUUIDListGV.as_view(), name='city-list'),
    path('city_uuid/<int:pk>/',  CityUUIDDetailGV.as_view(), name='city-details'),
    
    path('district/',  DistrictListGV.as_view(), name='district-list'),
    path('district/<int:pk>/',  DistrictDetailGV.as_view(), name='district-details'),
    path('district_uuid/',  DistrictUUIDListGV.as_view(), name='district-list'),
    path('district_uuid/<int:pk>/',  DistrictUUIDDetailGV.as_view(), name='district-details'),

    path('street/',  StreetListGV.as_view(), name='street-list'),
    path('street/<int:pk>/',  StreetDetailGV.as_view(), name='street-details'),
    path('street_uuid/',  StreetUUIDListGV.as_view(), name='street-list'),
    path('street_uuid/<int:pk>/',  StreetUUIDDetailGV.as_view(), name='street-details'),

    path('house/',  HouseListGV.as_view(), name='house-list'),
    path('house/<int:pk>/',  HouseDetailGV.as_view(), name='house-details'),
    path('house_uuid/',  HouseUUIDListGV.as_view(), name='house-list'),
    path('house_uuid/<int:pk>/',  HouseUUIDDetailGV.as_view(), name='house-details'),

    path('apartment/',  ApartmentListGV.as_view(), name='apartment-list'),
    path('apartment/<int:pk>/',  ApartmentDetailGV.as_view(), name='apartment-details'),
    path('apartment_uuid/',  ApartmentUUIDListGV.as_view(), name='apartment-list'),
    path('apartment_uuid/<int:pk>/',  ApartmentUUIDDetailGV.as_view(), name='apartment-details'),

    path('device/',  DeviceListGV.as_view(), name='device-list'),
    path('device/date_time_range/',  DeviceDateTimeRangeGV.as_view(), name='device-date-time-range'),
    path('device/<int:pk>/',  DeviceDetailGV.as_view(), name='device-details'),
    path('device/<int:pk>/download/',  DeviceDetailDownloadGV.as_view(), name='device-details-download'),
    path('device_uuid/',  DeviceUUIDListGV.as_view(), name='device-list'),
    path('device_uuid/<int:pk>/',  DeviceUUIDDetailGV.as_view(), name='device-details'),
    
    path('meter/',  MeterListGV.as_view(), name='meter-list'),
    path('meter/<int:pk>/',  MeterDetailGV.as_view(), name='meter-details'),
    path('meter_uuid/',  MeterUUIDListGV.as_view(), name='meter-list'),
    path('meter_uuid/<int:pk>/',  MeterUUIDDetailGV.as_view(), name='meter-details'),
]