# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from provedor.forms import LeadForm
from provedor.models import Lead


class LeadCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Lead
    form_class = LeadForm
    template_name = "provedor/lead_form.html"
    success_url = reverse_lazy("provedor:lead_form")
