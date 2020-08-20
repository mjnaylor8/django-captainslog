""" site urls """
from django.urls import path
from django.conf import settings
from triplog.views import SITEINFORMATIONView, AddSITEINFORMATIONView, ChangeSITEINFORMATIONView
from triplog.views import JOURNEYDETAILSView, AddJOURNEYDETAILSView, ChangeJOURNEYDETAILSView, AddJOURNEYDETAILS2View
mapbox_access_token = settings.MAPBOX_KEY


urlpatterns = [
    path("", AddJOURNEYDETAILSView.as_view(), name="addjourney"),
    path("test/", AddJOURNEYDETAILS2View.as_view(), name="addjourney2"),
    path("addsite/", AddSITEINFORMATIONView.as_view(), name="addsite"),
    path("site_information/<int:pk>", ChangeSITEINFORMATIONView.as_view(), name="changesite"),
    path("journey_details/<int:pk>", ChangeJOURNEYDETAILSView.as_view(), name="changejourney"),
    path("siteindex/", SITEINFORMATIONView.as_view(), name="siteindex"),
    path("journeyindex/", JOURNEYDETAILSView.as_view(), name="journeyindex"),

]
