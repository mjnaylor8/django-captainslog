from django.shortcuts import render

# Create your views here.
from django.views.generic import  View, CreateView, UpdateView, ListView

from .models import Site_Information, Journey_Details


class AddSite_InformationView(CreateView):
    model = Site_Information
    template_name = "triplog/site_information_form.html"
    success_url = "/siteindex/"
    fields = ("location", "address",)


class ChangeSite_InformationView(UpdateView):
    model = Site_Information
    template_name = "triplog/site_information_form.html"
    success_url = "/siteindex/"
    fields = ("location", "address",)


class Site_InformationView(ListView):
    model = Site_Information
    template_name = "triplog/siteindex.html"
    ordering = ["-created_at", ]

class Journey_DetailsView(ListView):
    model = Journey_Details
    template_name = "triplog/journeyindex.html"
    success_url = "/journeyindex/"
    ordering = ["-start_date",]

class AddJourney_DetailsView(CreateView):
    model = Journey_Details
    template_name = "triplog/journey_details_form.html"
    success_url = "/journeyindex/"
    fields = "__all__" 

class ChangeJourney_DetailsView(UpdateView):
    model = Journey_Details
    template_name = "triplog/journey_details_form.html"
    success_url = "/journeyindex/"
    fields = "__all__"    