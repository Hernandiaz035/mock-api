"""Clients Model."""

# Django
from django.db import models


class Client(models.Model):
    """Client Model.

    Contains all the client information."""

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with this email already exists.'
        }
    )

    driving_licence = models.CharField(max_length=20)

    ip_address = models.GenericIPAddressField(protocol='IPv4')

    city = models.CharField(max_length=50)

    def __str__(self):
        """Returns email."""

        return self.email

