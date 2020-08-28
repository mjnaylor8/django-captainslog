"""
defines the forms for triplog
"""
import datetime
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset, Field
from crispy_forms.bootstrap import TabHolder, Tab
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from triplog.models import SiteInformation, JourneyDetails






STANDARD_COLUMN_CLASS = 'form-group col-md-2 mb-0'
STANDARD_COLUMN_CLASS_WIDER = 'form-group col-md-4 mb-0'
STANDARD_COLUMN_CLASS_EVENWIDER = 'form-group col-md-8 mb-0'
STANDARD_COLUMN_CLASS_FULLWIDTH = 'form-group col-md-12 mb-0'
CSS_CLASS_FORMROW = 'form-row'
ENTER_STARTING_LOCATION = 'Please enter the starting location'
class SiteInformationForm(forms.ModelForm):
    """
    define the site information
    """
    class Meta:
        model = SiteInformation
        fields = "__all__"

class JourneyDetailsForm(forms.ModelForm):
    """ define the journey details """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-journeydetailsForm'
        self.helper.form_method = 'post' # get or post
        self.helper.add_input(Submit('submit', 'Save Journey', css_class='btn-primary'))
        self.fields['start_date'].initial = datetime.date.today
        self.fields['end_date'].initial = datetime.date.today
        self.fields['start_date'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['end_date'].input_formats = settings.DATE_INPUT_FORMATS

        self.helper.layout = Layout(
            TabHolder(
                Tab("Journey Details",
                    Fieldset(
                        'Dates',
                        Row(
                            Column('start_date', css_class=STANDARD_COLUMN_CLASS),
                            Column('end_date', css_class=STANDARD_COLUMN_CLASS),
                            css_class=CSS_CLASS_FORMROW
                            ),
                        ),
                    Fieldset(
                        'Journey',
                        Row(
                            Column('travel_from', css_class=STANDARD_COLUMN_CLASS_WIDER),
                            Column('travel_to', css_class=STANDARD_COLUMN_CLASS_WIDER),
                            css_class=CSS_CLASS_FORMROW
                            ),
                        Row(
                            Column('mileage_start', css_class=STANDARD_COLUMN_CLASS),
                            Column('mileage_end', css_class=STANDARD_COLUMN_CLASS),
                            Column('distance', css_class=STANDARD_COLUMN_CLASS),
                            css_class=CSS_CLASS_FORMROW
                            ),
                        ),
                    Fieldset(
                        'Destination',
                        Field('destination', css_class=STANDARD_COLUMN_CLASS_WIDER),
                        Row(
                            Column('star_rating', css_class=STANDARD_COLUMN_CLASS),
                            Column('would_return', css_class=STANDARD_COLUMN_CLASS)
                        ),
                        Field('notes', css_class=STANDARD_COLUMN_CLASS_EVENWIDER),
                        ),
                    ),
                Tab("Further Details",
                    Row(
                        Column('weather', css_class=STANDARD_COLUMN_CLASS_FULLWIDTH)
                    ),
                    Fieldset(
                        'Times',
                        Row(
                            Column('start_time', css_class=STANDARD_COLUMN_CLASS),
                            Column('end_time', css_class=STANDARD_COLUMN_CLASS),
                            Column('duration', css_class=STANDARD_COLUMN_CLASS),
                            css_class=CSS_CLASS_FORMROW
                            ),
                        ),
                    Fieldset(
                        'Costs',
                        Row(
                            Column('toll_currency', css_class=STANDARD_COLUMN_CLASS),
                            Column('toll_charges', css_class=STANDARD_COLUMN_CLASS),
                            css_class=CSS_CLASS_FORMROW
                            ),
                        ),
                    )
                )
            )
    class Meta:
        model = JourneyDetails
        fields = "__all__"
        labels = {
            'start_date': _('Start Date'),
            'end_date': _('End Date'),
            'travel_from': _('Travel From'),
            'travel_to': _('Travel To'),
            'mileage_start': _('Start Mileage'),
            'mileage_end': _('End Mileage'),
            'start_time': _('Start Time'),
            'end_time': _('End Time'),
            'destination': _('Destination Site'),
            'star_rating': _('Star Rating'),
            }
        help_texts = {
            'start_date': _('Enter a start date'),
            'end_date': _('Enter a end date'),
            'travel_from': ENTER_STARTING_LOCATION,
            'travel_to': _('Enter destination name'),
            'mileage_start': _('Enter start mileage'),
            'mileage_end': _('Enter end mileage'),
            'destination': _('Select the site destination'),
            'star_rating': _('Select the number of stars to give the destination'),
            }
        error_messages = {
            'travel_from': {
                'required': ENTER_STARTING_LOCATION, \
                },
            }
        widgets = {
            'start_date': DatePickerInput(
                format='%d-%m-%Y',
                attrs={
                    'class': 'form-control',
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                    'type': 'text',
                    },
                options={
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }),
            'end_date': DatePickerInput(
                format='%d-%m-%Y',
                attrs={
                    'class': 'form-control',
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                    'type':'text',
                    },
                options={
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }),
            'notes': forms.Textarea(attrs={'placeholder': 'Enter Notes on the journey and site', \
                'class': 'form-control'}),
            'travel_from' : forms.TextInput(attrs={'placeholder': 'Starting Point', \
                'class': 'form-control', \
                'oninvalid' : str('%s%s%s') % \
                    ('this.setCustomValidity("', ENTER_STARTING_LOCATION, '")'),\
                'oninput' : 'setCustomValidity("")'}),
            'travel_to' : forms.TextInput(attrs={'placeholder': 'Destination', \
                'class': 'form-control'}),
            'weather' : forms.TextInput(attrs={'placeholder': 'What was the weather like?', \
                'class': 'form-control'}),
            'start_time': TimePickerInput(
                attrs={
                    'class': 'form-control',
                    'append': 'fa fa-clock-o',
                    'icon_toggle': True,},),
            'end_time': TimePickerInput(
                attrs={
                    'class': 'form-control',
                    'append': 'fa fa-clock-o',
                    'icon_toggle': True,},)
            }
    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(JourneyDetailsForm, self).clean()

        # extract the fields from the data
        mileage_start = self.cleaned_data.get('mileage_start')
        mileage_end = self.cleaned_data.get('mileage_end')
        travel_from = self.cleaned_data.get('travel_from')
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')


        # conditions to be met
        if mileage_start and mileage_end:
            if mileage_start >= mileage_end:
                raise ValidationError \
                    ("The ending mileage must be greater than the starting mileage")

        if len(travel_from) < 2:
            raise ValidationError \
                ("The starting point must have more than 1 character!")

        if end_date and end_date < start_date:
            raise ValidationError \
                ("The end date must be the same or later than the start date")    

        # return any errors if found
        return self.cleaned_data
