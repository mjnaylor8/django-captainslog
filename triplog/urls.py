""" site urls """
from django.urls import path
from django.conf import settings
from .views import \
    SiteInformationView, AddSiteInformationView, ChangeSiteInformationView, Site2InformationView, \
    JourneyDetailView, AddJourneyDetailView, Journey2DetailsView, ChangeJourneyDetailView, \
    Trip2DetailView, AddTripDetailView, ChangeTripDetailView, \
    index
mapbox_access_token = settings.MAPBOX_KEY


urlpatterns = [
    path("", index, name="index"),
    path("addsite/", AddSiteInformationView.as_view(), name="addsite"),
    path("site_information/<int:pk>", ChangeSiteInformationView.as_view(), name="changesite"),
    path("addjourney", AddJourneyDetailView.as_view(), name="addjourney"),
    path("journey_details/<int:pk>", ChangeJourneyDetailView.as_view(), name="changejourney"),
    path("siteindex/", SiteInformationView.as_view(), name="siteindex"),
    path("site2index/", Site2InformationView.as_view(), name="site2index"),
    path("journeyindex/", JourneyDetailView.as_view(), name="journeyindex"),
    path("journey2index/", Journey2DetailsView.as_view(), name="journey2index"),
    path("addtrip/", AddTripDetailView.as_view(), name="addtrip"),
    path("trip_details/<int:pk>", ChangeTripDetailView.as_view(), name="changetrip"),
    path("trip2index/", Trip2DetailView.as_view(), name="trip2index"),
]
