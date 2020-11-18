""" base urls  """
from django.urls import path
#from django.conf.urls import include, url
#from djgeojson.views import GeoJSONLayerView
#from django.contrib import admin
#from sitemaps.models import sites
from . import views


app_name = 'sitemaps'

urlpatterns = [
    path('', views.default_map, name="default"),
    path('gl/', views.gl_map, name="default"),
]
