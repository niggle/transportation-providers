from rest_framework import generics

from service_areas.models import ServiceArea
from service_areas.serializers import ServiceAreaSerializer


class ServiceAreaListCreateView(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.select_related('provider').all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceArea.objects.select_related('provider').all()
    serializer_class = ServiceAreaSerializer
