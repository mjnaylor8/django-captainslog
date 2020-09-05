""" Admin defined """
from django.contrib.gis import admin
from mapbox_location_field.spatial.admin import SpatialMapAdmin
from triplog.models import SiteInformation, JourneyDetails


# Register models.

@admin.register(SiteInformation)
class SiteInformationAdmin(SpatialMapAdmin):
    """ Admin for SiteInformation defined """
    list_display = ("name", "address", "location")
    ordering = ("name",)
    search_fields = ("name",)
    readonly_fields = ("created_date", "edited_date")

@admin.register(JourneyDetails)
class JourneyDetailsAdmin(admin.ModelAdmin):
    """ Admin for JourneyDetails defined """
    list_display = ("start_date", "travel_from", "travel_to")
    search_fields = ("start_date",)
    readonly_fields = ("created_date", "edited_date")
