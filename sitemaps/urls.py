from django.urls import path
from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib import admin
from sitemaps.models import sites


app_name = 'sitemaps'

urlpatterns = [
    path('', views.default_map, name="default"),
]   

