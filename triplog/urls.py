from django.contrib import admin
from django.urls import re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from triplog.views import Site_InformationView, AddSite_InformationView, ChangeSite_InformationView
mapbox_access_token = settings.MAPBOX_KEY



urlpatterns = [
    re_path("^$", AddSite_InformationView.as_view(), name="add"),
    re_path("^site_information/(?P<pk>[0-9]+)/$", ChangeSite_InformationView.as_view(), name="change"),
    re_path("^index/$", Site_InformationView.as_view(), name="index"),

] 