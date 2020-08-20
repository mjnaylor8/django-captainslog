"""
defines the forms for triplog
"""
import datetime
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset, Field




from triplog.models import SITEINFORMATION, SITEFACILITIES, JOURNEYDETAILS

STANDARD_COLUMN_CLASS = 'form-group col-md-2 mb-0'
STANDARD_COLUMN_CLASS_WIDER = 'form-group col-md-4 mb-0'
STANDARD_COLUMN_CLASS_EVENWIDER = 'form-group col-md-8 mb-0'
class SITEINFORMATIONForm(forms.ModelForm):
    """
    define the site information
    """
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-journeydetailsForm'
        self.helper.form_method = 'post' # get or post
        self.helper.add_input(Submit('submit', 'Save Journey', css_class='btn-primary'))
        self.fields['start_date'].initial = datetime.date.today
        self.fields['end_date'].initial = datetime.date.today
        self.helper.layout = Layout(
            Fieldset(
                'Dates',
                Row(
                    Column('start_date', css_class=STANDARD_COLUMN_CLASS),
                    Column('end_date', css_class=STANDARD_COLUMN_CLASS),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Journey',
                Row(
                    Column('travel_from', css_class=STANDARD_COLUMN_CLASS_WIDER),
                    Column('travel_to', css_class=STANDARD_COLUMN_CLASS_WIDER),
                    css_class='form-row'
                ),
                Row(
                    Column('mileage_start', css_class=STANDARD_COLUMN_CLASS),
                    Column('mileage_end', css_class=STANDARD_COLUMN_CLASS),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Destination',
                Field('destination', css_class=STANDARD_COLUMN_CLASS_WIDER),
                Field('star_rating', css_class=STANDARD_COLUMN_CLASS),
                Field('notes', css_class=STANDARD_COLUMN_CLASS_EVENWIDER),
            ),
        )
    class Meta:
        model = JOURNEYDETAILS
        fields = "__all__"
        labels = {
            'start_date': _("Start Date"),
            'end_date': _("End Date"),
            }
        help_texts = {
            'start_date': _('Enter a start date'),
            'end_date': _('Enter a end date'),
            'travel_from': _('Enter starting location'),
            'travel_to': _('Enter destination name'),
            'mileage_start': _('Enter start mileage'),
            'mileage_end': _('Enter destination mileage'),
            }
        error_messages = {
            }
        widgets = {
            'start_date': forms.TextInput(attrs={'type':'date'}),
            'end_date': forms.TextInput(attrs={'type':'date'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Enter Notes on the journey and site'}),
            'travel_from' : forms.TextInput(attrs={'placeholder': 'Starting Point'}),
            'travel_to' : forms.TextInput(attrs={'placeholder': 'Destination'})
            }

class JOURNEYDETAILS2Form(forms.ModelForm):
    """ define the journey details """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].initial = datetime.date.today
        self.fields['end_date'].initial = datetime.date.today

    class Meta:
        model = JOURNEYDETAILS
        fields = "__all__"
        labels = {
            'start_date': _("Start Date"),
            'end_date': _("End Date"),
            }
        help_texts = {
            'start_date': _('Enter a start date'),
            'end_date': _('Enter a end date'),
            'travel_from': _('Enter starting location'),
            'travel_to': _('Enter destination name'),
            'mileage_start': _('Enter start mileage'),
            'mileage_end': _('Enter end mileage'),
            'destination': _('Enter destination'),
            'star_rating': _('Select the number of stars to give the destiantion'),
            }
        error_messages = {

            }
        widgets = {
            'start_date': forms.TextInput(attrs={'type':'date', \
                'class': 'form-control'}),
            'end_date': forms.TextInput(attrs={'type':'date', \
                'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Enter Notes on the journey and site', \
                'class': 'form-control'}),
            'travel_from' : forms.TextInput(attrs={'placeholder': 'Starting Point', \
                'class': 'form-control'}),
            'travel_to' : forms.TextInput(attrs={'placeholder': 'Destination', \
                'class': 'form-control'}),
            }
    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(JOURNEYDETAILS2Form, self).clean()

        # extract the username and text field from the data
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        travel_from = self.cleaned_data.get('travel_from')
        mileage_start = self.cleaned_data.get('mileage_start')
        mileage_end = self.cleaned_data.get('mileage_end')
        destination = self.cleaned_data.get('destination')
        star_rating = self.cleaned_data.get('star_rating')

        # conditions to be met
        if mileage_start and mileage_end:
            if mileage_start >= mileage_end:
                raise ValidationError \
                    ("The ending mileage must be greater than the starting mileage")
        if not travel_from:
            raise ValidationError("The starting point must be entered")
        # return any errors if found
        return self.cleaned_data
