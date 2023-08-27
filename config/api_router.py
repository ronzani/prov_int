from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from base.api.v1.views import LoginView
from prov_int.users.api.views import UserViewSet

# from rest_auth.views import LoginView


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

app_name = "api"

urlpatterns = router.urls

urlpatterns += [
    path(
        "login/",
        LoginView.as_view(),
        name="rest_login",
    ),
    path(
        "refresh-token/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("v1/", include("provedor.api.v1.urls")),
]
