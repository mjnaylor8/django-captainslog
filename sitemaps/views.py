""" Views """
import json
import os
from os.path import join



from django.urls import reverse_lazy
from django.shortcuts import (
    render,
    get_object_or_404)
from django.conf import settings
from django.core import serializers
from django.contrib import messages
from django.core.files.base import (
    ContentFile, 
    File)
from django.http import (
    JsonResponse, 
    HttpResponse,
    HttpResponseRedirect)
from django.views.generic import (
    DeleteView,
    CreateView,
    UpdateView,
    ListView,
    FormView,
    TemplateView)
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django_tables2 import SingleTableView
from more_itertools import unique_everseen
from itertools import chain
from guardian.utils import get_anonymous_user

from triplog.models import SiteInformation, TripDetail, JourneyDetail
from sitemaps.models import GeoJSONRoute
from sitemaps.tables import GeoJSONRouteTable
from sitemaps.forms import GeoJSONRouteModelForm



# Defines the map default
def default_map(request):
    """ Defines the map default """
    mapbox_access_token = settings.MAPBOX_KEY
    return render(request, 'sitemaps/index.html',
                  {'mapbox_access_token': mapbox_access_token})

def drawroute_map(request):
    """ Defines the map default """
    mapbox_access_token = settings.MAPBOX_KEY
    return render(request, 'sitemaps/drawroute.html',
                  {'mapbox_access_token': mapbox_access_token})

#Defines a MapBox GL map
def site_map(request):
    """ Defines a MapBox GL map """
    mapbox_access_token = settings.MAPBOX_KEY
    sites_visited = SiteInformation.objects.order_by("name")
    trips_taken = TripDetail.objects.order_by("name")
    journeys_done = JourneyDetail.objects.order_by("-start_date")
    return render(request, 'sitemaps/map.html',
                  {'mapbox_access_token': mapbox_access_token,
                   'sites_visited': sites_visited,
                   'trips_taken': trips_taken,
                   'journeys_done': journeys_done,
                  })

#Defines a MapBox GL map
def store_map(request):
    """ Defines a MapBox GL map """
    mapbox_access_token = settings.MAPBOX_KEY
    sites_visited = SiteInformation.objects.order_by("name")
    return render(request, 'sitemaps/mapboxstore.html',
                  {'mapbox_access_token': mapbox_access_token,
                   'sites_visited' : sites_visited,
                  })

#Defines a MapBox GL map
def test(request):
    """ Defines a MapBox GL map """
    mapbox_access_token = settings.MAPBOX_KEY
    sites_visited = SiteInformation.objects.order_by("name")
    return render(request, 'sitemaps/test.html',
                  {'mapbox_access_token': mapbox_access_token,
                   'sites_visited' : sites_visited,
                  })

#Defines the trip site view filter
def load_tripsites(request):
    """ Defines an ajax call for map """
    trip_id = request.GET.get('trip')
    site_journeys_from = JourneyDetail.objects.filter \
        (trip=trip_id).values_list('travel_from', flat=True).order_by("start_date")
    site_journeys_to = JourneyDetail.objects.filter \
        (trip=trip_id).values_list('travel_to', flat=True)
    unique_sites = list(unique_everseen(sorted(chain(site_journeys_from, site_journeys_to))))
    sites_visited = SiteInformation.objects.filter(id__in=unique_sites).order_by("name")
    data = serializers.serialize("json", sites_visited)
    return HttpResponse(data)

def save_route(request):
    """ Defines an ajax PUT for trip route """
    if request.is_ajax():
        if request.method == 'PUT':
            # Get user and check if logged in
            if request.user.is_anonymous:
                request.user = get_anonymous_user()
                # return HttpResponse(json.dumps({'msg': ("Please login to save and update routes!")}))
            # Get the data from the PUT
            body_unicode = request.body.decode('utf-8')
            route_file = json.loads(body_unicode)
            # Set up the name and path to save as
            file_name = route_file['name']
            # path = join(settings.MEDIA_ROOT, 'routes', file_name + '.json')
            path = 'routes' + "/" + str(request.user.id).zfill(2) + "/"
            filename = path + file_name + '.geojson'
            allroutes = None
            if not GeoJSONRoute.objects.filter(route_name=file_name, route_file=filename).exists():
                route = GeoJSONRoute.objects.create(route_name=file_name)
            else:
                allroutes = GeoJSONRoute.objects.filter(route_name=file_name, route_file=filename)
                route = allroutes[0]
            data = route_file['file']
            content_file = ContentFile(json.dumps(data))
            route.route_file = content_file
            route.user = request.user
            route.route_file.save(file_name + '.geojson', content_file)
            
            if allroutes is None:
                return HttpResponse(JsonResponse({'msg': ('A new route object has been created with the same name as the file. File ' + file_name + '.geojson' + ' written to ' + join(settings.MEDIA_ROOT, 'routes', str(request.user.id).zfill(2)))}))
            if allroutes.count() > 1:
                return HttpResponse(JsonResponse({'msg': ('There are ' + str(allroutes.count()) + ' routes with the same name ' + file_name + ' and filename. ' + file_name + '.geojson' + ' written to ' + join(settings.MEDIA_ROOT, 'routes', str(request.user.id).zfill(2)))}))
            if allroutes.count() == 1:
                return HttpResponse(JsonResponse({'msg': ('The route with the name ' + file_name + ' has been updated with ' + file_name + '.geojson' + ' written to ' + join(settings.MEDIA_ROOT, 'routes', str(request.user.id).zfill(2)))}))
  
                
def get_route_names(request):
    
    if request.method == 'GET':
        geojson_routes = GeoJSONRoute.objects.all()
        data = serializers.serialize("json", geojson_routes, fields=("pk", "route_name", "route_description", "route_file"))
        return HttpResponse(data)

def get_all_route_data(request):
    
    if request.method == 'GET':
        geojson_routes = GeoJSONRoute.objects.filter().values("route_name", "route_description").order_by("route_name")
        data = serializers.serialize("json", geojson_routes, fields=("pk", "route_name", "route_description"))
        return HttpResponse(data)

def get_route_data(request):
    
    if request.method == 'GET':
        record_key = request.GET.get('record_key')
        geojson_routes = GeoJSONRoute.objects.get(id=record_key)
        route_data = geojson_routes.route_file.read()
        return HttpResponse(route_data)

class AjaxTemplateMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        called_byfetch = 'Call-From' in request.headers
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax() or (called_byfetch and request.headers['Call-From'] == 'fetch'):
            self.template_name = self.ajax_template_name
            # self.table_pagination = False
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

# RouteView
class GeoJSONRouteDetailView(SuccessMessageMixin, AjaxTemplateMixin, SingleTableView):
    """ List route details view """
    model = GeoJSONRoute
    table_class = GeoJSONRouteTable
    template_name = "sitemaps/list_route_table.html"
    paginate_by = 10

    def get_initial(self):
        return (self)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DeleteGeoJSONRouteView(SuccessMessageMixin, AjaxTemplateMixin, DeleteView):
    model = GeoJSONRoute
    template_name = 'sitemaps/delete_route.html'
    success_message = 'Success: Route %(route_name)s was deleted.'
    success_url = '/maps/routetable'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        if self.request.is_ajax():
            data = {
                'message': "Successfully deleted route."
            }
            super().delete(request, *args, **kwargs)
            return JsonResponse(data)
        else:
            return super().delete(request, *args, **kwargs)

class CreateGeoJSONRouteView(SuccessMessageMixin, AjaxTemplateMixin, CreateView):
    model = GeoJSONRoute
    template_name = 'sitemaps/create_route.html'
    success_message = 'Success: Route %(route_name)s was created.'
    success_url = '/maps/routetable'
    fields = '__all__'


    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully created route."
            }
            return JsonResponse(data)
        else:
            return response
    


class UpdateGeoJSONRouteView(SuccessMessageMixin, AjaxTemplateMixin, UpdateView):
    """ change route view """
    model = GeoJSONRoute
    template_name = 'sitemaps/update_route.html'
    success_message = 'Success: Route %(route_name)s was updated.'
    form_class = GeoJSONRouteModelForm
    route = None
    
    def get_initial(self):
        self.route = get_object_or_404(GeoJSONRoute, pk=self.kwargs.get('pk'))
        return {'route': self.route,}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['route'] = self.route
        return context


    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted updated route."
            }
            return JsonResponse(data)
        else:
            return response
    # def update(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     messages.success(self.request, self.success_message % obj.__dict__)
    #     return super().update(request, *args, **kwargs)

    # def GeoJSONRoute_edit(request, pk):
    #     if request.method == 'POST':
    #         form = GeoJSONRouteModelForm(instance=GeoJSONRoute, data=request.POST)
    #         if form.is_valid():
    #             form.save()
    #     else:
    #         form = GeoJSONRouteModelForm(instance=GeoJSONRoute)
    #     return render(request, template, {
    #         'GeoJSOnRoute': GeoJSONRoute,
    #         'form': form,
    #     })

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            # self.success_url = '/maps/updateroute/' + str(self.kwargs['pk'])
            self.success_url = '/maps/routetable'
            route = GeoJSONRoute.objects.get(id=str(self.kwargs['pk']))
            form = GeoJSONRouteModelForm(data=request.POST, files=request.FILES, instance=route)
            # path = 'routes' + "/" + str(request.user.id).zfill(2) + "/"
            if form.is_valid():
                form.user = request.user
                form.route_name = form.cleaned_data['route_name']
                form.route_description = form.cleaned_data['route_description']
                form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            form = GeoJSONRouteModelForm()
        return render(request, '/sitemaps/update_route.html', {'form': form})
