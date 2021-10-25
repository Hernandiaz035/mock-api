"""Clients URLs."""

# Django
from django.urls import path

# Views
from mock_api.clients.views import (
    ClientListView,
    ClientDetailView,
)


urlpatterns = [
    path("", view=ClientListView.as_view(), name="clients-list"),
    path("<int:pk>", view=ClientDetailView.as_view(), name="clients-detail"),
]
