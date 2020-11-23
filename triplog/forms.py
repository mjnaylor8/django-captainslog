"""
defines the forms for triplog
"""
import datetime
from django import forms
from django.conf import settings
from django.db.models import Q
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, Div
from crispy_forms.bootstrap import TabHolder, Tab, InlineRadios, PrependedText
from triplog.models import SiteInformation, JourneyDetail, TripDetail

STANDARD_COLUMN_CLASS = 'col-md-2 mb-0'
STANDARD_COLUMN_CLASS_WIDER = 'col-md-4 mb-0'
STANDARD_COLUMN_CLASS_ABITWIDER = 'col-md-6 mb-0'
STANDARD_COLUMN_CLASS_EVENWIDER = 'col-md-8 mb-0'
STANDARD_COLUMN_CLASS_FULLWIDTH = 'col-md-12 mb-0'
CSS_CLASS_FORMROW = 'form-row'
ENTER_STARTING_LOCATION = 'Please enter the starting location'

class SiteInformationForm(forms.ModelForm):
    """ define the site information """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-sitedetailsForm'
        self.helper.form_method = 'post' # get or post
        self.helper.add_input(Submit('submit', 'Save Site', css_class='btn-primary btn-sm ml-4'))
        self.fields['star_rating'].initial = 0
        self.fields['would_return'].initial = True
        self.fields['ambience'].empty_label = "n/a"
        self.helper.layout = Layout(
            TabHolder(
                Tab("Site Location",
                    Row(
                        Column('name', css_class=STANDARD_COLUMN_CLASS_WIDER),
                        Column('star_rating', css_class='col-md-3 mb-0')
                    ),
                    Row(
                        Column('siteowner', css_class=STANDARD_COLUMN_CLASS),
                        Column('days_stayed', css_class='col-md-1 mb-0'),
                        Column(PrependedText('cost_charges',
                                             mark_safe('<i class="fas fa-pound-sign"></i>')), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        InlineRadios('would_return', css_class='col-md-2 mb-0')
                    ),
                    Row(
                        Column('notes', css_class=STANDARD_COLUMN_CLASS_FULLWIDTH)
                    ),
                    Row(
                        Column('location', css_class=STANDARD_COLUMN_CLASS_FULLWIDTH),
                        Column('address', css_class=STANDARD_COLUMN_CLASS_FULLWIDTH)
                    ),
                    ),
                Tab("Further Details",
                    Row(
                        Column(PrependedText('email',
                                             mark_safe('<i class="fas fa-at"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS_WIDER),
                        Column(PrependedText('phone_number',
                                             mark_safe('<i class="fas fa-phone"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('cost_extras',
                                             mark_safe('<i class="fas fa-pound-sign"></i>')), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('cost_currency',
                                             mark_safe('<i class="fas fa-money"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                    ),
                    Row(
                        Column(PrependedText('greeting',
                                             mark_safe('<i class="far fa-handshake"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('ambience',
                                             mark_safe('<i class="fas fa-volume-down"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('security',
                                             mark_safe('<i class="fas fa-lock"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS)
                    ),
                    Row(
                        Column('pitch_type', css_class=STANDARD_COLUMN_CLASS),
                        Column('pitch_level', css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('hook_up',
                                             mark_safe('<i class="fas fa-plug"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('toilets',
                                             mark_safe('<i class="fas fa-toilet"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('waste',
                                             mark_safe('<i class="fas fa-dumpster"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS)
                    ),
                    Row(
                        Column(PrependedText('wifi',
                                             mark_safe('<i class="fas fa-wifi"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('tv_signal',
                                             mark_safe('<i class="fas fa-satellite-dish"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('phone_signal_3G_4G',
                                             mark_safe('<i class="fas fa-signal"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS)
                    ),
                    Row(
                        Column(PrependedText('pets',
                                             mark_safe('<i class="fas fa-paw"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('children',
                                             mark_safe('<i class="fas fa-child"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS),
                        Column(PrependedText('laundry',
                                             mark_safe('<i class="mdi mdi-local-laundry-service mdi-lg"></i>'),
                                             active=True), \
                                             css_class=STANDARD_COLUMN_CLASS)
                    ),
                    ),
            ),
        )
        super(SiteInformationForm, self).__init__(*args, **kwargs)
    class Meta:
        model = SiteInformation
        fields = "__all__"
        labels = {
            'tv_signal': _('TV Signal'),
            'wifi': _('Wi-Fi'),
            'phone_signal_3G_4G': _('Phone Signal'),
        }
        help_texts = {
            'star_rating': _('Select the number of stars to give the destination'),
        }
        widgets = {
            'notes': forms.Textarea(attrs={'placeholder': 'Enter Notes on the site', \
                'class': 'form-control', 'rows': 4}),
            'star_rating': forms.NumberInput(attrs={'class': 'rating rating-loading krajee-fas', \
                'step': 0.5, 'data-size': 'sm', 'dir': 'ltr'}),
            'would_return': forms.RadioSelect(attrs={'class': 'form-check-inline'}),
            'cost_currency': forms.Select(attrs={'onchange': 'getCurrency();'})
            }

class JourneyDetailForm(forms.ModelForm):
    """ define the journey details """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['travel_from'].queryset = SiteInformation.objects.order_by('name')
        self.fields['travel_to'].queryset = SiteInformation.objects.order_by('name')
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-journeydetailForm'
        self.helper.form_method = 'post' # get or post
        self.helper.add_input(Submit('submit', 'Save Journey', css_class='btn-primary btn-sm ml-4'))
        self.fields['start_date'].initial = datetime.date.today
        self.fields['end_date'].initial = datetime.date.today
        self.fields['start_date'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['end_date'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['start_time'].initial = datetime.datetime.now
        self.fields['end_time'].initial = datetime.datetime.now
        self.fields['duration'].initial = "00:00"
        self.fields['start_time'].input_formats = settings.TIME_INPUT_FORMATS
        self.fields['end_time'].input_formats = settings.TIME_INPUT_FORMATS
        self.helper.layout = Layout(

            Tab("Journey Details",
                Row(
                    Column('travel_from', css_class='col-md-3 mb-0'),
                    Column('travel_to', css_class='col-md-3 mb-0'),
                    ),
                Row(
                    Column('start_date', css_class=STANDARD_COLUMN_CLASS),
                    Column('start_time', css_class='col-md-1 mb-0'),
                ),
                Row(
                    Column('end_date', css_class=STANDARD_COLUMN_CLASS),
                    Column('end_time', css_class='col-md-1 mb-0'),
                    Column('duration', css_class='col-md-1 mb-0'),
                    ),
                Row(
                    Column('mileage_start', css_class='col-md-1 mb-0'),
                    Column('mileage_end', css_class='col-md-1 mb-0'),
                    Column('distance', css_class='col-md-1 mb-0'),
                    ),
                Row(
                    Column('notes', css_class=STANDARD_COLUMN_CLASS_ABITWIDER),
                ),
                Row(
                    Column(PrependedText('toll_currency',
                                         mark_safe('<i class="fas fa-money"></i>'),
                                         active=True), \
                                         css_class=STANDARD_COLUMN_CLASS),
                    Column(PrependedText('toll_charges',
                                         mark_safe('<i class="fas fa-pound-sign"></i>')), \
                                         css_class=STANDARD_COLUMN_CLASS),
                    ),
                )
        )
        super(JourneyDetailForm, self).__init__(*args, **kwargs)
    class Meta:
        model = JourneyDetail
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
            }
        error_messages = {
            'travel_from': {
                'required': ENTER_STARTING_LOCATION, \
                },
            }
        widgets = {
            'start_date': forms.DateInput(
                attrs={
                    'data-role': 'datebox',
                    'data-options': '{"mode":"calbox","overrideDateFormat":"%d/%m/%Y", \
                        "closeCallback":"datelinker","closeCallbackArgs":["id_end_date"]}',
                    'rows': 1,
                    'readonly': 'readonly'
                }),
            'end_date': forms.DateInput(
                attrs={
                    'data-role': 'datebox',
                    'data-options': '{"mode":"calbox","overrideDateFormat":"%d/%m/%Y"}',
                    'rows': 1,
                    'readonly': 'readonly'
                }),
            'start_time': forms.TimeInput(
                attrs={
                    'data-role': 'datebox',
                    'data-options': '{"mode":"timebox","overrideDateFormat":"%H:%M",\
                        "closeCallback":"timelinker","closeCallbackArgs":["id_end_time"]}',
                    'rows': 1,
                    'readonly': 'readonly',
                    'onchange': 'setDuration();',
                }),
            'end_time': forms.TimeInput(
                attrs={
                    'data-role': 'datebox',
                    'data-options': '{"mode":"timebox","overrideDateFormat":"%H:%M",\
                        "closeCallback":"setDuration", \
                        "closeCallbackArgs":["id_start_time","id_end_time"]}',
                    'rows': 1,
                    'readonly': 'readonly',
                    'onchange': 'setDuration();',
                }),
            'duration': forms.TextInput(
                attrs={
                    'data-role': 'datebox',
                    'data-options': '{"mode":"durationbox","useButton": false, \
                        "hideinput": true, "overrideDurationFormat":"%Dl:%DM", \
                        "beforeOpenCallback":"setDuration", \
                        "beforeOpenCallbackArgs":["id_start_time","id_end_time"]}',
                    'rows': 1,
                    'readonly': 'readonly',
                    'class': 'text-sm-right',
                }
                ),
            'mileage_start': forms.NumberInput(
                attrs={
                    'onchange': 'setDistance();',
                }
            ),
            'mileage_end': forms.NumberInput(
                attrs={
                    'onchange': 'setDistance();',
                }
            ),
            'distance': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'text-sm-right',
                }
            ),
            'notes': forms.Textarea(attrs={'placeholder': 'Enter Notes on the journey', \
                'class': 'form-control', \
                'onchange': 'checkTime();'}),
            'weather' : forms.TextInput(attrs={'placeholder': 'What was the weather like?', \
                'class': 'form-control'}),

            'toll_currency': forms.Select(attrs={'onchange': 'getCurrency();'})
            }

    # this function will be used for the validation of duration
    # duration is shown without seconds on form and so when
    # passed through is thought by validation to be of format mm:ss when it is actually hh:mm
    # multiplying this by 60 gives total seconds correctly
    def clean_duration(self):
        """ clean duration so it is formatted correctly """
        data = self.cleaned_data['duration']
        data = data * 60
        return data

    # this function will be used for the validation of the form
    def clean(self):
        # data from the form is fetched using super function
        super(JourneyDetailForm, self).clean()

        # extract the fields from the data
        mileage_start = self.cleaned_data.get('mileage_start')
        mileage_end = self.cleaned_data.get('mileage_end')
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')


        # conditions to be met
        if mileage_start and mileage_end:
            if mileage_start >= mileage_end:
                raise ValidationError \
                    ("The ending mileage must be greater than the starting mileage")

        if end_date and end_date < start_date:
            raise ValidationError \
                ("The end date must be the same or later than the start date")

        # return any errors if found
        return self.cleaned_data

class LoginWithPlaceholder(AuthenticationForm):
    """ Login Form """
    def __init__(self, *args, **kwargs):
        super(LoginWithPlaceholder, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(Div(Field('username',
                                              placeholder='username'), \
                                              css_class="form-group"),
                                    Div(Field('password',
                                              placeholder='password'), \
                                              css_class="form-group"),
                                    Div(Submit('submit', 'Log in')))

class TripDetailForm(forms.ModelForm):
    """ define the journey details """
    journeychoice = forms.ModelMultipleChoiceField(
        queryset=JourneyDetail.objects.filter(trip__isnull=True).order_by("start_date"), \
        required=False, label="Select one or more Journeys", \
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial')
        currentjourneys = initial.get('currentjourneys')
        existing = JourneyDetail.objects.filter(trip=currentjourneys).values_list('id')
        criterion1 = Q(id__in=existing)
        criterion2 = Q(trip__isnull=True)

        self.helper = FormHelper(self)
        self.helper.form_id = 'id-tripdetailsForm'
        self.helper.form_method = 'post' # get or post
        self.helper.add_input(Submit('submit', 'Save Trip', css_class='btn-primary btn-sm ml-4'))
        self.helper.layout = Layout(

            Tab("Trip Details",
                Row(
                    Column('name', css_class='col-md-3 mb-0'),
                ),
                Row(
                    Column('description', css_class='col-md-9 mb-0'),
                ),

                Row('journeychoice'),
                ),
        )
        self.fields['journeychoice'].queryset = \
            JourneyDetail.objects.filter(criterion1 | criterion2).order_by("-start_date")
        if currentjourneys is not None:
            self.fields['journeychoice'].initial = list(existing.values_list('id', flat=True))
    class Meta:
        model = TripDetail
        fields = "__all__"
        labels = {
            'name': _('Trip Name'),
            'journeychoice': _('Select one or more Journeys'),
            }
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Enter Notes on the trip', \
                'class': 'form-control', 'rows': 4}),
            'journeychoice': forms.widgets.SelectMultiple(),
            'currentjourneys': forms.HiddenInput,
            }

    def save(self, commit=True):
        trip = self.instance
        trip.name = self.cleaned_data['name']
        trip.description = self.cleaned_data['description']
        return trip
