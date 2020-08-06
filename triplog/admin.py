from django.contrib import admin
import floppyforms as forms
from triplog.models import Site_Information, Site_Facilities, Journey_Details
from floppyforms.gis import PointWidget, BaseOsmWidget
from django.forms import ModelForm

# Register your models here.

class CustomPointWidget(PointWidget, BaseOsmWidget):
    class Media:
        js = ('/static/floppyforms/js/MapWidget.js',)

class Site_InformationAdminForm(ModelForm):
    class Meta:
            model = Site_Information
            fields = [
                'name',
                'address_line1',
                'address_line2',
                'address_line3',
                'address_code',
                'location',
                'email',
                'phone_number'
            ]
            widgets = {
                'location': CustomPointWidget
            }
class Site_InformationAdmin (admin.ModelAdmin):
    form = Site_InformationAdminForm

admin.site.register(Site_Information, Site_InformationAdmin)
admin.site.register(Site_Facilities)
admin.site.register(Journey_Details)
