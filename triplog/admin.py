""" Admin defined """
from django.contrib.gis import admin
from triplog.forms import SiteInformationForm
from mapbox_location_field.spatial.admin import SpatialMapAdmin
from triplog.models import SiteInformation, JourneyDetail, TripDetail, TripJourneyInline


# Register models.

@admin.register(SiteInformation)
class SiteInformationAdmin(SpatialMapAdmin):
    """ Admin for SiteInformation defined """
    # class Meta:
    #     model = SiteInformation
    #     widgets = {
    #         "location": "mapbox_location_field.widgets.MapInput"
    #     }
    form = SiteInformationForm
    add_exclude = ("address", "addressline", "locality", "place", "district", \
        "postcode", "region", "country")
    edit_exclude = ("address", "addressline", "locality", "place", "district", \
        "postcode", "region", "country")
    list_display = ("name", "address", "country", "location")
    ordering = ("name",)
    search_fields = ("name",)
    readonly_fields = ("created_date", "edited_date")
    def add_view(self, request, form_url='', extra_context=None):
        self.exclude = getattr(self, 'add_exclude', ())
        return super(SiteInformationAdmin, self).add_view(request, form_url, \
            extra_context=extra_context, )
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.exclude = getattr(self, 'edit_exclude', ())
        return super(SiteInformationAdmin, self).change_view(request, object_id, \
            form_url, extra_context=extra_context, )

@admin.register(JourneyDetail)
class JourneyDetailAdmin(admin.ModelAdmin):
    """ Admin for JourneyDetail defined """
    list_display = ("start_date", "travel_from", "travel_to")
    search_fields = ("start_date",)
    readonly_fields = ("created_date", "edited_date")

@admin.register(TripDetail)
class TripDetailAdmin(admin.ModelAdmin):
    """ Admin for TripDetails defined """
    inlines = (TripJourneyInline,)
