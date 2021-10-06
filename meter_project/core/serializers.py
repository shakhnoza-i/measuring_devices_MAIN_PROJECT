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


class CitySerializer(serializers.ModelSerializer):

    districts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        depth = 2
        model = City
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):

    streets = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = District
        fields = "__all__"


class StreetSerializer(serializers.ModelSerializer):

    houses = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Street
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):

    apartments = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = House
        fields = "__all__"


class ApartmentSerializer(serializers.ModelSerializer):

    device = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Apartment
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):

    meter = UUIDRelatedField(many=True, queryset=Meter.objects.all(), uuid_field='uuid')
    
    class Meta:
        model = Device
        fields = "__all__"


class MeterSerializer(serializers.ModelSerializer):

    #apartment = serializers.CharField(source='apartment.name')
    
    class Meta:
        model = Meter
        fields = "__all__"
