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
    ordering = ("name",)
    search_fields = ("name",)



@admin.register(Journey_Details)
class Journey_DetailsAdmin(admin.ModelAdmin):
    list_display = ("start_date", "travel_from", "travel_to", "created_date")
    search_fields = ("start_date",)

#@admin.register(Site_Facilities)
class Site_FacilitiesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Site_Facilities, Site_FacilitiesAdmin)