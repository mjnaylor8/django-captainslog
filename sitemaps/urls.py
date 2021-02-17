""" base urls  """
from django.urls import path, re_path
#from django.conf.urls import include, url
#from djgeojson.views import GeoJSONLayerView
#from django.contrib import admin
#from sitemaps.models import sites
from sitemaps.views import (
    default_map,
    site_map,
    store_map,
    test,
    drawroute_map,
    load_tripsites,
    save_route,
    get_route_names,
    get_route_data,
    get_all_route_data,
    UpdateGeoJSONRouteView,
    CreateGeoJSONRouteView,
    DeleteGeoJSONRouteView,
    GeoJSONRouteDetailView
)


app_name = 'sitemaps'

urlpatterns = [
    path('', default_map, name="default"),
    path('sites/', site_map, name="sitemap"),
    path('store/', store_map, name="default"),
    path('test/', test, name="default"),
    path('drawroute/', drawroute_map, name="drawroute"),
    path('ajax/load-tripsites/', load_tripsites, name='ajax_load_tripsites'),
    path('ajax/save-route/', save_route, name='ajax_save_route'),
    path('ajax/get-route-names/', get_route_names, name='ajax_get_route_names'),
    path('ajax/get-all-route-data/', get_all_route_data, name='ajax_get_all_route_data'),
    path('ajax/get-route-data/', get_route_data, name='ajax_get_route_data'),
    path('routetable/', GeoJSONRouteDetailView.as_view(), name='routetable'),
    path('updateroute/<int:pk>', UpdateGeoJSONRouteView.as_view(), name='updateroute'),
    path('deleteroute/<int:pk>', DeleteGeoJSONRouteView.as_view(), name='deleteroute'),
    path('createroute/', CreateGeoJSONRouteView.as_view(), name='createroute')
]
