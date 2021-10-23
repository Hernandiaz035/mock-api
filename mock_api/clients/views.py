"""Clients Views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Serializers
from mock_api.clients.serializers import ClientModelSerializer

# Models
from mock_api.clients.models import Client


class ClientsViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """Clients View Set."""

    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
