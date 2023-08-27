from django.urls import include, path
from rest_framework.routers import SimpleRouter

from provedor.api.v1.views import LeadView, ProvedorView

router = SimpleRouter()

router.register(r"provedor", ProvedorView, basename="provedor")
router.register(r"lead", LeadView, basename="lead")


urlpatterns = [
    path("", include(router.urls)),
]
