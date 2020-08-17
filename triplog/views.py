

# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView, FormView

from .models import SITEINFORMATION, JOURNEYDETAILS


class AddSITEINFORMATIONView(CreateView):
    model = SITEINFORMATION
    template_name = "triplog/site_information_form.html"
    success_url = "/siteindex/"
    fields = ("name", "location", "address",)


class ChangeSITEINFORMATIONView(UpdateView):
    model = SITEINFORMATION
    template_name = "triplog/site_information_form.html"
    success_url = "/siteindex/"
    fields = ("name", "location", "address",)


class SITEINFORMATIONView(ListView):
    model = SITEINFORMATION
    template_name = "triplog/siteindex.html"
    ordering = ["-created_at", ]

class JOURNEYDETAILSView(ListView):
    model = JOURNEYDETAILS
    template_name = "triplog/journeyindex.html"
    success_url = "/journeyindex/"
    ordering = ["-start_date",]

class AddJOURNEYDETAILSView(CreateView):
    model = JOURNEYDETAILS
    template_name = "triplog/journey_details_form.html"
    success_url = "/journeyindex/"
    fields = "__all__"

class ChangeJOURNEYDETAILSView(UpdateView):
    model = JOURNEYDETAILS
    template_name = "triplog/journey_details_form.html"
    success_url = "/journeyindex/"
    fields = "__all__"
