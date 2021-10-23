"""Clients Test."""

# Django
from django.test import TestCase

# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Models
from mock_api.clients.models import Client


class ClientsCreationTest(TestCase):
    """Client Creation Test."""

    def setUp(self):
        """Test Case Set up."""
        self.c = Client.objects.create(
            first_name = "John",
            last_name = "Doe",
            email = "john.doe@example.com",
            city = "NY",
            ip_address = "8.8.8.8",
            driving_licence = "123456789123456",
        )

    def test_client_creation(self):
        """Test Client Creation."""
        c = Client.objects.create(
            first_name = "John",
            last_name = "Doe",
            email = "john.doe0@example.com",
            city = "NY",
            ip_address = "8.8.8.8",
            driving_licence = "123456789123456",
        )

        self.assertIsNotNone(c)

    def test_client_persistance(self):
        """Test Client Persistance."""
        c = Client.objects.get(email="john.doe@example.com")
        self.assertEqual(c.email, "john.doe@example.com")


class ClientsApiCrud(APITestCase):
    """Clients API CRUD Test."""

    def setUp(self):
        """Test Case Set up."""
        self.c = Client.objects.create(
            first_name = "John",
            last_name = "Doe",
            email = "john.doe@example.com",
            city = "NY",
            ip_address = "8.8.8.8",
            driving_licence = "123456789123456",
        )

    def test_api_retrieve(self):
        """Test API client Retrieve."""
        url = f"/clients/{self.c.id}/"
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_api_creation(self):
        """Test API Client Creation."""
        url = f"/clients/"
        request = self.client.post(
            url,
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe1@example.com",
                "city": "NY",
                "ip_address": "8.8.8.8",
                "driving_licence": "123456789123456",
            }
        )

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
