from django.contrib.gis import admin
from mapbox_location_field.spatial.admin import SpatialMapAdmin
from triplog.models import SITEINFORMATION, SITEFACILITIES, JOURNEYDETAILS


# Register your models here.


@admin.register(SITEINFORMATION)
class SITEINFORMATIONAdmin(SpatialMapAdmin):
    list_display = ("name", "address", "location", "created_at")
    ordering = ("name",)
    search_fields = ("name",)



@admin.register(JOURNEYDETAILS)
class JOURNEYDETAILSAdmin(admin.ModelAdmin):
    list_display = ("start_date", "travel_from", "travel_to", "created_date")
    search_fields = ("start_date",)

#@admin.register(Site_Facilities)
class SITEFACILITIESAdmin(admin.ModelAdmin):
    pass

admin.site.register(SITEFACILITIES, SITEFACILITIESAdmin)
