from django.contrib.gis.geos import Point
from rest_framework import generics

from service_areas.models import ServiceArea
from service_areas.serializers import ServiceAreaSerializer


class ServiceAreaListCreateView(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.select_related('provider').all()
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        """
        filter a aervice area if the point in query param, given by lat and lng, is inside the area.
        lat and lng needs to be an integer or a float with a dot
        """
        queryset = self.queryset
        longitude = self.request.query_params.get('lng', None)
        latitude = self.request.query_params.get('lat', None)
        if longitude and latitude:
            coordinates = Point(float(longitude), float(latitude))
            queryset = queryset.filter(area__contains=coordinates)
        return queryset


class ServiceAreaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceArea.objects.select_related('provider').all()
    serializer_class = ServiceAreaSerializer
