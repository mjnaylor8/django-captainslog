from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView

from .models import Site_Information


class AddSite_InformationView(CreateView):
    model = Site_Information
    template_name = "triplog/site_information_form.html"
    success_url = "/index/"
    fields = ("location", "address")


class ChangeSite_InformationView(UpdateView):
    model = Site_Information
    template_name = "triplog/site_information_form.html"
    success_url = "/index/"
    fields = ("location", "address")


class Site_InformationView(ListView):
    model = Site_Information
    template_name = "triplog/index.html"
    ordering = ["-created_at", ]