from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from service_areas.models import ServiceArea


# area geojson format
#  '{"type":"Polygon","coordinates":[[[-6.0, 40.0],[-5.0, 40.0],[-5.0, 38.0],[-7.0, 37.0],[-6.0, 40.0]]]}'
class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider_name = serializers.SerializerMethodField()

    class Meta:
        model = ServiceArea
        geo_field = "area"
        fields = ('name', 'price', 'provider', 'provider_name')

    def get_provider_name(self, obj):
        return obj.provider.name
