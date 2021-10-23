"""Clients Views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Serializers
from mock_api.clients.serializers import ClientModelSerializer, ClientSummarySerializer

# Models
from mock_api.clients.models import Client


class ClientsViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """Clients View Set."""

    queryset = Client.objects.all()
    serializer_class = ClientSummarySerializer

    def list(self, request, *args, **kwargs):
        self.get_serializer = ClientSummarySerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.get_serializer = ClientModelSerializer
        return super().retrieve(request, *args, **kwargs)
