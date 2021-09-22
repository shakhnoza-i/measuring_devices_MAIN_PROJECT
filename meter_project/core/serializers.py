from rest_framework import serializers
from core.models import City, District, Street, House, Apartment, Device, Meter


class CitySerializer(serializers.ModelSerializer):

    district = serializers.StringRelatedField(many=True, read_only=True) # StringRelated - return what we defined in __str__
    #district = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):

    #locate = serializers.CharField(sourse = 'locate.name')
    street = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = District
        exclude = ('locate',)


class StreetSerializer(serializers.ModelSerializer):

    house = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Street
        exclude = ('locate',)


class HouseSerializer(serializers.ModelSerializer):

    apartment = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = House
        exclude = ('locate',)


class ApartmentSerializer(serializers.ModelSerializer):

    device = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Apartment
        exclude = ('locate',)


class DeviceSerializer(serializers.ModelSerializer):

    meter = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Device
        exclude = ('locate',)


class MeterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Meter
        exclude = ('locate',)
