from django import forms
from triplog.models import Site_Information

class Site_InformationForm(forms.ModelForm):
    class Meta:
        model = Site_Information
        fields = "__all__"