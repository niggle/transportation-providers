from rest_framework import generics

from providers.models import Provider
from providers.serializers import ProviderSerializer


class ProviderListCreateView(generics.ListCreateAPIView):
    """
        get:
        Lists  all the existing Providers.

        post:
        Create a new provider instance.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
        get:
        retrieve the Provider instance requested by id.

        put:
        Update a provider instance.

        delete:
        Delete a provider instance.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

