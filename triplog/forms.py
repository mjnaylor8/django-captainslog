""" defines the forms for triplog """
import datetime
from django import forms
from django.utils.translation import gettext_lazy as _


from triplog.models import SITEINFORMATION, SITEFACILITIES, JOURNEYDETAILS

class SITEINFORMATIONForm(forms.ModelForm):
    """ define the site information """
    class Meta:
        model = SITEINFORMATION
        fields = "__all__"

class SITEFACILITIESForm(forms.ModelForm):
    """ define the site facilities """
    class Meta:
        model = SITEFACILITIES
        fields = "__all__"

class JOURNEYDETAILSForm(forms.ModelForm):
    """ define the journey details """
    class Meta:
        model = JOURNEYDETAILS
        fields = "__all__"
        labels = {
            'start_date': _("Start Date"),
            'end_date': _("End Date"),
            }
        help_texts = {
            'start_date': _('Enter a start date'),
            }
        error_messages = {
            }
        widgets = {
            'start_date': forms.TextInput(attrs={'type':'date'}),
            'end_date': forms.TextInput(attrs={'type':'date'}),
            }
