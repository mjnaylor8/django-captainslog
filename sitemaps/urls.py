from django.conf.urls import url
from . import views
from django.contrib import admin


app_name = 'sitemaps'

urlpatterns = [
    url('', views.default_map, name="default"),
]

