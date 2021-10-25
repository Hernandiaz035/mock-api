"""Clients URLs."""

# Django
from django.urls import path

# Views
from mock_api.clients.views import (
    ClientListView,
)


urlpatterns = [
    path("", view=ClientListView.as_view(), name="clients-list"),
]
