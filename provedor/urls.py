from django.urls import path

from provedor.views import LeadCreateView

app_name = "provedor"

urlpatterns = [
    path("lead-add/", view=LeadCreateView.as_view(), name="lead_add"),
]
