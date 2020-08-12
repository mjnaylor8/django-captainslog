from django.contrib.gis import admin
from triplog.models import Site_Information, Site_Facilities, Journey_Details
from django.forms import ModelForm
from mapbox_location_field.spatial.admin import SpatialMapAdmin

# Register your models here.

#class Site_InformationAdminForm(ModelForm):
#    class Meta:
#        model = Site_Information

#        fields = "__all__"
#class Site_InformationAdmin ():
#    form = Site_InformationAdminForm


@admin.register(Site_Information)
class Site_informationAdmin(SpatialMapAdmin):
    list_display = ("name", "address", "location", "created_at")
    search_fields = ("name", "location",)

#admin.site.register(Site_informationAdmin, SpatialMapAdmin)


@admin.register(Journey_Details)
class Journey_DetailsAdmin(admin.ModelAdmin):
    list_display = ("start_date", "travel_from", "travel_to", "created_date")