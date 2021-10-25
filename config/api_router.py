from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

# Views
from mock_api.users.api.views import UserViewSet
from mock_api.clients.api.views import ClientsViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register(
    r'clients',
    ClientsViewSet,
    basename='clients'
)


app_name = "api"
urlpatterns = router.urls
