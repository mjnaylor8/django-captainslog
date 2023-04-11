""" Define Models """
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from mapbox_location_field.spatial.models import SpatialLocationField
from mapbox_location_field.models import \
    AddressAutoHiddenField, AddressCountryField, AddressRegionField, \
    AddressDistrictField, AddressPlaceField, AddressLocalityField, AddressPostcodeField, \
    AddressLineField

# Create your models here.

class TripDetail(models.Model):
    """ Define TripDetail Model """
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True, null=True)
    trip_route = models.FileField(upload_to='media/', blank=True, null=True)
    uploaded_trip_route_at = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        blank=True, null=True, related_name='trip_created_by')
    edited_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        blank=True, null=True, related_name='trip_edited_by')

    def __str__(self):
        return self.name

class CurrencyChoice(models.TextChoices):
    """ Define Currency Choices """
    EUR = "EUR", _("€")
    GBP = "GBP", _("£")
    USD = "USD", _("$")
    CHF = "CHF", _("CHF")
class SiteOwnerChoice(models.TextChoices):
    """ Define Site Owner Choices """
    CAMC_CL = "CAMC CL", _("CAMC CL")
    CAMC_SITE = "CAMC Site", _("CAMC Site")
    CACC_CL = "C&CC CL", _("C&CC CL")
    CACC_SITE = "C&CC Site", _("C&CC Site")
    INDEPENDENT = "Independent", _("Independent")
    FRANCE_PASSION = "France Passion", _("France Passion")
    AIRE = "Aire", _("Aire")
    PUB = "Pub", _("Pub")
    HOTEL = "Hotel", _("Hotel")
    RESTAURANT = "Restaurant", _("Restaurant")
    ROADSIDE = "Roadside", _("Roadside")
    HOME = "Home", _("Home")
    NA = "n/a", _("n/a")
class GreetingChoice(models.TextChoices):
    """ Define Greeting Choices """
    EXCELLENT = "Excellent", _("Excellent")
    GOOD = "Good", _("Good")
    INDIFFERENT = "Indifferent", _("Indifferent")
class PitchTypeChoice(models.TextChoices):
    """ Define Pitch Type Choices """
    DIRT = "Dirt", _("Dirt")
    GRASS = "Grass", _("Grass")
    HARDSTANDING = "Hardstanding", _("Hardstanding")
class PitchLevelChoice(models.TextChoices):
    """ Define Pitch Level Choices """
    LEVEL = "Level", _("Level")
    GENTLE_SLOPE = "Gentle Slope", _("Gentle Slope")
    STEEP_SLOPE = "Steep Slope", _("Steep Slope")
    IMPOSSIBLE_SLOPE = "Impossible Slope", _("Impossible Slope")
class HookUpChoice(models.TextChoices):
    """ Define Hook Up Choices """
    SIX_AMP = "6A", _("6A")
    TEN_AMP = "10A", _("10A")
    SIXTEEN_AMP = "16A", _("16A")
class WasteChoice(models.TextChoices):
    """ Define Waste Choices """
    ON_PITCH = "On Pitch", _("On Pitch")
    CLOSE_BY = "Close By", _("Close By")
    MILES_AWAY = "Miles Away", _("Miles Away")
class ToiletChoice(models.TextChoices):
    """ Define Toilet Choices """
    NONE = "None", _("None")
    CLEAN = "Clean", _("Clean")
    DIRTY = "Dirty", _("Dirty")
    DONT_GO_THERE = "Don't Go There", _("Don't Go There")
class AmbianceChoice(models.TextChoices):
    """ Define Ambience Choices """
    PEACEFUL = "Peaceful", _("Peaceful")
    OKAY = "OK", _("OK")
    LOUD_LIVELY = "Loud/Lively", _("Loud/Lively")
class SecurityChoice(models.TextChoices):
    """ Define Security Choices """
    EXCELLENT = "Excellent", _("Excellent")
    GOOD = "Good", _("Good")
    POOR = "Poor", _("Poor")
class TVSignalChoice(models.TextChoices):
    """ Define TV Signel Choices """
    EXCELLENT = "Excellent", _("Excellent")
    GOOD = "Good", _("Good")
    POOR = "Poor", _("Poor")
    NA = "n/a", _("n/a")
class PhoneSignalChoice(models.TextChoices):
    """ Define Phone Signal Choices """
    EXCELLENT4 = "Excellent 4G", _("Excellent 4G")
    GOOD4 = "Good 4G", _("Good 4G")
    POOR4 = "Poor 4G", _("Poor 4G")
    EXCELLENT3 = "Excellent 3G", _("Excellent 3G")
    GOOD3 = "Good 3G", _("Good 3G")
    POOR3 = "Poor 3G", _("Poor 3G")


class AutoDateTimeField(models.DateTimeField):
    """ Define Current Timezone Choices """
    def pre_save(self, model_instance, add):
        return timezone.now()


class SiteInformation(models.Model):
    """ Define SiteInformation Model """

    TRUE_FALSE_CHOICES = [
        (True, "Yes"),
        (False, "No"),
        (None, "n/a")
    ]

    name = models.CharField(max_length=256)
    address = AddressAutoHiddenField(blank=True, null=True, map_id="map_1")
    addressline = AddressLineField(blank=True, null=True, map_id="map_1")
    locality = AddressLocalityField(blank=True, null=True, map_id="map_1")
    place = AddressPlaceField(blank=True, null=True, map_id="map_1")
    district = AddressDistrictField(blank=True, null=True, map_id="map_1")
    postcode = AddressPostcodeField(blank=True, null=True, map_id="map_1")
    region = AddressRegionField(blank=True, null=True, map_id="map_1")
    country = AddressCountryField(blank=True, null=True, map_id="map_1")
    email = models.CharField(max_length=256, blank=True)
    siteowner = models.CharField(max_length=256, blank=True, \
        choices=SiteOwnerChoice.choices, default=SiteOwnerChoice.NA)
    phone_number = models.CharField(max_length=256, blank=True)
    location = SpatialLocationField(null=True, blank=True, map_attrs={
        "id": "map_1",
        "center": [-0.827610, 51.182250],
        "placeholder": "Pick a location on the map below",
        "style": "mapbox://styles/mapbox/satellite-streets-v11"
        })
    #star_rating = models.CharField(blank=True, \
    # choices=STAR_RATING_CHOICES, max_length=256, null=True)
    star_rating = models.DecimalField(max_digits=3, decimal_places=1, \
        blank=True, default=0, null=True)
    would_return = models.BooleanField(blank=True, null=True, \
        choices=TRUE_FALSE_CHOICES, default=True)
    greeting = models.CharField(max_length=256, blank=True, \
        choices=GreetingChoice.choices, default=GreetingChoice.GOOD)
    pitch_type = models.CharField(max_length=256, blank=True, \
        choices=PitchTypeChoice.choices, default=PitchTypeChoice.HARDSTANDING)
    pitch_level = models.CharField(max_length=256, blank=True, \
        choices=PitchLevelChoice.choices, default=PitchLevelChoice.LEVEL)
    hook_up = models.CharField(max_length=256, blank=True, \
        choices=HookUpChoice.choices, default=HookUpChoice.SIXTEEN_AMP)
    waste = models.CharField(max_length=256, blank=True, \
        choices=WasteChoice.choices, default=WasteChoice.CLOSE_BY)
    toilets = models.CharField(max_length=256, blank=True, \
        choices=ToiletChoice.choices, default=ToiletChoice.CLEAN)
    ambience = models.CharField(max_length=256, blank=True, \
        choices=AmbianceChoice.choices, default=AmbianceChoice.PEACEFUL)
    security = models.CharField(max_length=256, blank=True, \
        choices=SecurityChoice.choices, default=SecurityChoice.GOOD)
    wifi = models.BooleanField(null=True, blank=True, \
        choices=TRUE_FALSE_CHOICES, default=None)
    tv_signal = models.CharField(max_length=256, blank=True, \
        choices=TVSignalChoice.choices, default=TVSignalChoice.NA)
    phone_signal_3G_4G = models.CharField(max_length=256, blank=True, \
        choices=PhoneSignalChoice.choices, default=PhoneSignalChoice.GOOD4)
    pets = models.BooleanField(null=True, blank=True, \
        choices=TRUE_FALSE_CHOICES, default=True)
    children = models.BooleanField(null=True, blank=True, \
        choices=TRUE_FALSE_CHOICES, default=False)
    laundry = models.BooleanField(null=True, blank=True, \
        choices=TRUE_FALSE_CHOICES, default=False)
    cost_charges = models.DecimalField(max_digits=5, decimal_places=2, \
        null=True, blank=True)
    cost_extras = models.DecimalField(max_digits=5, decimal_places=2, \
        null=True, blank=True)
    cost_currency = models.CharField(max_length=3, blank=True, \
        choices=CurrencyChoice.choices, default=CurrencyChoice.GBP)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    days_stayed = models.IntegerField(blank=True, null=True, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        blank=True, null=True, related_name='site_created_by')
    edited_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        blank=True, null=True, related_name='site_edited_by')

    def __str__(self):
        return str(self.name)

    #def created_date(self):
    #    return self.created_date.strftime('%B %d %Y')

    #def edited_date(self):
    #    return self.edited_date.strftime('%B %d %Y')

    def get_absolute_url(self):
        """ Define absolute_url Model """
        return reverse('changesite', args=[str(self.id)])

class JourneyDetail(models.Model):
    """ Define JourneyDetail Model """

    TRUE_FALSE_CHOICES = [
        (True, "Yes"),
        (False, "No"),
        (None, "n/a")
    ]
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    weather = models.CharField(max_length=256, blank=True)
    trip = models.ForeignKey(TripDetail, \
        on_delete=models.DO_NOTHING, blank=True, null=True, related_name='journeydetails')
    travel_from = models.ForeignKey(SiteInformation, models.SET_NULL, \
        null=True, related_name='journey_travel_from')
    travel_to = models.ForeignKey(SiteInformation, models.SET_NULL, \
        null=True, blank=True, related_name='journey_travel_to')
    start_time = models.TimeField(blank=True, null=True,)
    end_time = models.TimeField(blank=True, null=True)
    #duration = models.TimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    mileage_start = models.IntegerField()
    mileage_end = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    toll_charges = models.FloatField(blank=True, null=True)
    toll_currency = models.CharField(max_length=3, blank=True, \
        choices=CurrencyChoice.choices, default=CurrencyChoice.GBP)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        blank=True, null=True, related_name='journey_created_by')
    edited_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        blank=True, null=True, related_name='journey_edited_by')


    def __str__(self):
#        return str('%s' % \
#            (self.start_date,))
        return str('%s, %s, %s' % \
            (self.start_date, self.travel_from, self.travel_to))

    #def created_date(self):
    #    return self.created_date.strftime('%B %d %Y')

    #def edited_date(self):
    #    return self.edited_date.strftime('%B %d %Y')

    def duration_HHmm(self):
        """ Define durationformat Model """
        sec = self.duration.total_seconds()
        return '%02d:%02d' % (int((sec/3600)%3600), int((sec/60)%60))

    def get_absolute_url(self):
        """ Define absolute_url Model """
        return reverse('changejourney', args=[str(self.id)])

class TripJourneyInline(admin.TabularInline):
    """ Define inline to allow Admin to work on Model """
    model = JourneyDetail
    extra = 5

class Author(models.Model):
    """ Define Author Model """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    bio = models.TextField(max_length=5000)

    def __str__(self):
        return str('%s %s' % (self.first_name, self.last_name))

class Image(models.Model):
    """ Define Image Model """
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='pictures/', blank=True)
    journey = models.ForeignKey(JourneyDetail, on_delete=models.CASCADE, \
        blank=True, null=True)
    site = models.ForeignKey(SiteInformation, on_delete=models.CASCADE, \
        blank=True, null=True)
    taken = models.DateTimeField(blank=True, null=True)
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """ Define Tag Model """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
