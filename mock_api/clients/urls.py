"""Clients URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from mock_api.clients.views import ClientsViewSet

router = DefaultRouter()
router.register(
    r'',
    ClientsViewSet,
    basename='clients'
)

urlpatterns = [
    path('', include(router.urls))
]
