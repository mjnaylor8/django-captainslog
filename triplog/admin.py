""" Admin defined """
from django.contrib.gis import admin
from mapbox_location_field.spatial.admin import SpatialMapAdmin
from triplog.models import SiteInformation, SiteFacilities, JourneyDetails


# Register models.

@admin.register(SiteInformation)
class SiteInformationAdmin(SpatialMapAdmin):
    """ Admin for SiteInformation defined """
    list_display = ("name", "address", "location", "created_at")
    ordering = ("name",)
    search_fields = ("name",)

@admin.register(JourneyDetails)
class JourneyDetailsAdmin(admin.ModelAdmin):
    """ Admin for JourneyDetails defined """
    list_display = ("start_date", "travel_from", "travel_to", "created_date")
    search_fields = ("start_date",)

#@admin.register(Site_Facilities)
class SiteFacilitiesAdmin(admin.ModelAdmin):
    """ Admin for JourneyFacilities defined """

admin.site.register(SiteFacilities, SiteFacilitiesAdmin)
