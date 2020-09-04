from django.shortcuts import render

# Create your views here.

from django.conf import settings

def default_map(request):
    mapbox_access_token = settings.MAPBOX_KEY
    return render(request, 'sitemaps/index.html',
                  {'mapbox_access_token': mapbox_access_token})
