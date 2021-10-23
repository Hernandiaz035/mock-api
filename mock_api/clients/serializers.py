"""Clients Serializer."""

# Django REST Framework
from rest_framework import serializers

# Model
from mock_api.clients.models import Client


class ClientModelSerializer(serializers.ModelSerializer):
    """Client Model Serializer."""

    class Meta:
        """Meta Class."""

        model = Client

        fields = '__all__'
