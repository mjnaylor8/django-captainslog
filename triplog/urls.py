""" site urls """
from django.urls import path
from django.conf import settings
from .views import SiteInformationView, AddSiteInformationView, ChangeSiteInformationView
from .views import JourneyDetailsView, AddJourneyDetailsView, \
    ChangeJourneyDetailsView, index
mapbox_access_token = settings.MAPBOX_KEY


urlpatterns = [
    path("", index, name="index"),
    path("addsite/", AddSiteInformationView.as_view(), name="addsite"),
    path("site_information/<int:pk>", ChangeSiteInformationView.as_view(), name="changesite"),
    path("addjourney/", AddJourneyDetailsView.as_view(), name="addjourney"),
    path("journey_details/<int:pk>", ChangeJourneyDetailsView.as_view(), name="changejourney"),
    path("siteindex/", SiteInformationView.as_view(), name="siteindex"),
    path("journeyindex/", JourneyDetailsView.as_view(), name="journeyindex"),
]
