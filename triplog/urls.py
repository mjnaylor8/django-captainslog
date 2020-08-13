from django.contrib import admin
from django.urls import re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from triplog.views import Site_InformationView, AddSite_InformationView, ChangeSite_InformationView, Journey_DetailsView, AddJourney_DetailsView, ChangeJourney_DetailsView
mapbox_access_token = settings.MAPBOX_KEY



urlpatterns = [
    re_path("^$", AddJourney_DetailsView.as_view(), name = "addjourney"),
    re_path("^addsite$", AddSite_InformationView.as_view(), name = "addsite"),
    re_path("^site_information/(?P<pk>[0-9]+)/$", ChangeSite_InformationView.as_view(), name = "changesite"),
    re_path("^journey_details/(?P<pk>[0-9]+)/$", ChangeJourney_DetailsView.as_view(), name = "changejourney"),
    re_path("^siteindex/$", Site_InformationView.as_view(), name = "siteindex"),
    re_path("^journeyindex/$", Journey_DetailsView.as_view(), name = "journeyindex")

] 