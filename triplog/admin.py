from django.contrib.gis import admin
from triplog.models import Site_Information, Site_Facilities, Journey_Details
from django.forms import ModelForm
from mapbox_location_field.spatial.admin import SpatialMapAdmin

# Register your models here.

#class Site_InformationAdminForm(ModelForm):
#    class Meta:
#        fields = "__all__"
#        model = Site_Information

#class Site_InformationAdmin (MapAdmin):
#    form = Site_InformationAdminForm

admin.site.register(Site_Information, SpatialMapAdmin)
admin.site.register(Journey_Details)
