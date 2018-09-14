from django.contrib.gis.geos import Point
from rest_framework import generics

from service_areas.models import ServiceArea
from service_areas.serializers import ServiceAreaSerializer


class ServiceAreaListCreateView(generics.ListCreateAPIView):
    """
        get:
        Return a list of all the existing ServiceArea.
        you can filter to return only areas that contain a given coordinate, you need to put lat and lng as a
        query param. ex.: /service-areas/?lat=0.01&lng=0.01

        post:
        Create a new Service Area instance.
        to send a new area ex.:
        {"type":"Polygon","coordinates":[[[-6.0, 40.0],[-5.0, 40.0],[-5.0, 38.0],[-7.0, 37.0],[-6.0, 40.0]]]}
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        """
        filter a aervice area if the point in query param, given by lat and lng, is inside the area.
        lat and lng needs to be an integer or a float with a dot
        """
        queryset = self.queryset.select_related('provider')
        longitude = self.request.query_params.get('lng', None)
        latitude = self.request.query_params.get('lat', None)
        if longitude and latitude:
            coordinates = Point(float(longitude), float(latitude))
            queryset = queryset.filter(area__contains=coordinates)
        return queryset


class ServiceAreaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
        get:
        Given an id retrieves the service area

        put:
        Update a service area by a given id
        to send a new area ex.:
        {"type":"Polygon","coordinates":[[[-6.0, 40.0],[-5.0, 40.0],[-5.0, 38.0],[-7.0, 37.0],[-6.0, 40.0]]]}

        patch:
        Update a service area by a given id
        to send a new area ex.:
        {"type":"Polygon","coordinates":[[[-6.0, 40.0],[-5.0, 40.0],[-5.0, 38.0],[-7.0, 37.0],[-6.0, 40.0]]]}

        delete:
        delete a service area by a given id
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
