from django import forms
from .models import GeoJSONRoute

class GeoJSONRouteModelForm(forms.ModelForm):
    class Meta:
        model = GeoJSONRoute
        fields = ['route_name', 'route_description', 'user', 'route_file']
        