""" Views """
from django.shortcuts import render
from django.conf import settings
from triplog.models import SiteInformation

# Defines the map default
def default_map(request):
    """ Defines the map default """
    mapbox_access_token = settings.MAPBOX_KEY
    return render(request, 'sitemaps/index.html',
                  {'mapbox_access_token': mapbox_access_token})

#Defines a MapBox GL map
def gl_map(request):
    """ Defines a MapBox GL map """
    mapbox_access_token = settings.MAPBOX_KEY
    sites_visited = SiteInformation.objects.order_by("name")
    return render(request, 'sitemaps/map.html',
                  {'mapbox_access_token': mapbox_access_token,
                   'sites_visited' : sites_visited,
                  })
