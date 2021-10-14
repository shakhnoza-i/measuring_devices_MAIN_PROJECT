from rest_framework import serializers
from core.models import City, District, Street, House, Apartment, Device, Meter
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.relations import RelatedField


class UUIDRelatedField(RelatedField):
    """
    A read-write field that represents the target of the relationship
    by a unique 'slug' attribute.
    """
    default_error_messages = {
        'does_not_exist': _('Object with {uuid_field}={value} does not exist.'),
        'invalid': _('Invalid value.'),
    }

    def __init__(self, uuid_field=None, **kwargs):
        assert uuid_field is not None, 'The `uuid_field` argument is required.'
        self.uuid_field = uuid_field
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(**{self.uuid_field: data})
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.uuid_field)
        except (TypeError, ValueError):
            self.fail('invalid')

    def to_representation(self, obj):
        return getattr(obj, self.uuid_field)



class MeterValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meter
        fields = ['uuid', 'initial_value', 'unit',]


class DeviceDateTimeRangeSerializer(serializers.ModelSerializer):

    meters = MeterValueSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = "__all__"


class MeterUUIDSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Meter
        exclude = ['full_owner', 'part_owner', 'full_owner_link', 'part_owner_link',]
        #fields = "__all__"


class DeviceUUIDSerializer(serializers.ModelSerializer):

    meters = UUIDRelatedField(many=True, queryset=Meter.objects.all(), uuid_field='uuid')
    
    class Meta:
        model = Device
        fields = ['name', 'meters']


class ApartmentUUIDSerializer(serializers.ModelSerializer):
    devices = DeviceUUIDSerializer(many=True, read_only=True)
    
    class Meta:
        model = Apartment
        fields = ['name', 'devices']


class HouseUUIDSerializer(serializers.ModelSerializer):

    apartments = ApartmentUUIDSerializer(many=True, read_only=True)
    
    class Meta:
        model = House
        fields = ['name', 'apartments']


class StreetUUIDSerializer(serializers.ModelSerializer):

    houses = HouseUUIDSerializer(many=True, read_only=True)

    class Meta:
        model = Street
        fields = ['name', 'houses']


class DistrictUUIDSerializer(serializers.ModelSerializer):

    streets = StreetUUIDSerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = ['name', 'streets']


class CityUUIDSerializer(serializers.ModelSerializer):

    districts = DistrictUUIDSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['name', 'districts']



class CitySerializer(serializers.ModelSerializer):

    districts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = City
        #exclude = ['full_owner', 'part_owner', 'full_owner_link', 'part_owner_link',]
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):

    streets = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = District
        exclude = ['full_owner', 'part_owner', 'full_owner_link', 'part_owner_link',]


class StreetSerializer(serializers.ModelSerializer):

    houses = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Street
        exclude = ['full_owner', 'part_owner', 'full_owner_link', 'part_owner_link',]


class HouseSerializer(serializers.ModelSerializer):

    apartments = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = House
        exclude = ['full_owner', 'part_owner', 'full_owner_link', 'part_owner_link',]


class ApartmentSerializer(serializers.ModelSerializer):

    device = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Apartment
        exclude = ['full_owner', 'part_owner', 'full_owner_link', 'part_owner_link',]


class DeviceSerializer(serializers.ModelSerializer):

    meter = UUIDRelatedField(many=True, queryset=Meter.objects.all(), uuid_field='uuid')
    
    class Meta:
        model = Device
        exclude = ['full_owner', 'part_owner', 'full_owner_link', 'part_owner_link',]


class MeterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Meter
        exclude = ['full_owner', 'part_owner', 'full_owner_link', 'part_owner_link',]
