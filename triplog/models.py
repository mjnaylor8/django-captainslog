""" Define Models """
from django.contrib.gis.db import models
from mapbox_location_field.spatial.models import SpatialLocationField
from mapbox_location_field.models import AddressAutoHiddenField

# Create your models here.

class SiteInformation(models.Model):
    """ Define SiteInformation Model """
    EXCELLENT = "Excellent"
    GOOD = "Good"
    INDIFFERENT = "Indifferent"
    DIRT = "DIRT"
    GRASS = "Grass"
    HARDSTANDING = "Hardstanding"
    LEVEL = "Level"
    GENTLE_SLOPE = "Gentle Slope"
    STEEP_SLOPE = "Steep Slope"
    IMPOSSIBLE_SLOPE = "Impossible Slope"
    SIX_AMP = "6A"
    TEN_AMP = "10A"
    SIXTEEN_AMP = "16A"
    ON_PITCH = "On Pitch"
    CLOSE_BY = "Close By"
    MILES_AWAY = "Miles Away"
    NONE = "None"
    CLEAN = "Clean"
    DIRTY = "Dirty"
    DONT_GO_THERE = "Don't Go There"
    PEACEFUL = "Peaceful"
    OKAY = "OK"
    LOUD_LIVELY = "Loud / Lively"
    POOR = "Poor"

    GREETING_CHOICES = [
        (EXCELLENT, "Excellent"),
        (GOOD, "Good"),
        (INDIFFERENT, "Indifferent"),
    ]

    PITCH_TYPE_CHOICES = [
        (DIRT, "Dirt"),
        (GRASS, "Grass"),
        (HARDSTANDING, "Hardstanding"),
    ]

    PITCH_LEVELS_CHOICES = [
        (LEVEL, "Level"),
        (GENTLE_SLOPE, "Gentle Slope"),
        (STEEP_SLOPE, "Steep Slope"),
        (IMPOSSIBLE_SLOPE, "Impossible Slope"),
    ]

    HOOK_UP_CHOICES = [
        (SIX_AMP, "6A"),
        (TEN_AMP, "10A"),
        (SIXTEEN_AMP, "16A"),
    ]

    WASTE_CHOICES = [
        (ON_PITCH, "On Pitch"),
        (CLOSE_BY, "Close By"),
        (MILES_AWAY, "Miles Away"),
    ]

    TOILET_CHOICES = [
        (NONE, "None"),
        (CLEAN, "Clean"),
        (DIRTY, "Dirty"),
        (DONT_GO_THERE, "Don't Go There"),
    ]

    AMBIENCE_CHOICES = [
        (PEACEFUL, "Peaceful"),
        (OKAY, "OK"),
        (LOUD_LIVELY, "Loud / Lively"),
    ]

    SECURITY_CHOICES = [
        (GOOD, "Good"),
        (POOR, "Poor"),
    ]

    TV_SIGNAL_CHOICES = [
        (GOOD, "Good"),
        (POOR, "Poor"),
    ]
    PHONE_SIGNAL_3G_4G_CHOICES = [
        (GOOD, "Good"),
        (POOR, "Poor"),
    ]
    TRUE_FALSE_CHOICES = [
        (True, "Yes"),
        (False, "No")
    ]

    name = models.CharField(max_length=256)
    address = AddressAutoHiddenField()
    email = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=256, blank=True)
    location = SpatialLocationField(null=True, blank=True, map_attrs={
        "center": [-0.827610, 51.182250],
        "placeholder": "Pick a location on the map below",
        })
    greeting = models.CharField(max_length=256, blank=True, choices=GREETING_CHOICES)
    pitch_type = models.CharField(max_length=256, blank=True, choices=PITCH_LEVELS_CHOICES)
    pitch_level = models.CharField(max_length=256, blank=True, choices=PITCH_LEVELS_CHOICES)
    hook_up = models.CharField(max_length=256, blank=True, choices=HOOK_UP_CHOICES)
    waste = models.CharField(max_length=256, blank=True, choices=WASTE_CHOICES)
    toilets = models.CharField(max_length=256, blank=True, choices=TOILET_CHOICES)
    ambience = models.CharField(max_length=256, blank=True, choices=AMBIENCE_CHOICES)
    security = models.CharField(max_length=256, blank=True, choices=SECURITY_CHOICES)
    wifi = models.BooleanField(null=True,blank=True, choices=TRUE_FALSE_CHOICES)
    tv_signal = models.CharField(max_length=256, blank=True, choices=TV_SIGNAL_CHOICES)
    phone_signal_3G_4G = models.CharField(max_length=256, blank=True, \
        choices=PHONE_SIGNAL_3G_4G_CHOICES)
    pets = models.BooleanField(null=True,blank=True, choices=TRUE_FALSE_CHOICES)
    children = models.BooleanField(null=True,blank=True, choices=TRUE_FALSE_CHOICES)
    laundry = models.BooleanField(null=True,blank=True, choices=TRUE_FALSE_CHOICES)
    cost_charges = models.FloatField(null=True,blank=True)
    cost_extras = models.FloatField(null=True,blank=True)
    cost_currency = models.CharField(max_length=3, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class JourneyDetails(models.Model):
    """ Define JourneyDetails Model """

    ONESTAR = '*'
    TWOSTAR = '**'
    THREESTAR = '***'
    FOURSTAR = '****'
    FIVESTAR = '*****'
    STAR_RATING_CHOICES = [
        ('', 'Choose...'),
        (ONESTAR, "One Star"),
        (TWOSTAR, "Two Star"),
        (THREESTAR, "Three Star"),
        (FOURSTAR, "Four Star"),
        (FIVESTAR, "Five Star"),
    ]
    TRUE_FALSE_CHOICES = [
        (True, "Yes"),
        (False, "No")
    ]
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    weather = models.CharField(max_length=256, blank=True)
    travel_from = models.CharField(max_length=256)
    travel_to = models.CharField(max_length=256, blank=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    mileage_start = models.FloatField()
    mileage_end = models.FloatField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    toll_charges = models.FloatField(blank=True, null=True)
    toll_currency = models.CharField(max_length=3, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    edited_date = models.DateTimeField(auto_now_add=True, null=True)
    star_rating = models.CharField(choices=STAR_RATING_CHOICES, max_length=256)
    would_return = models.BooleanField(blank=True, choices=TRUE_FALSE_CHOICES, null=True)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    destination = models.ForeignKey(SiteInformation, models.SET_NULL, null=True)

    def __str__(self):
        return str('%s - %s - %s - %s' % \
            (self.start_date, self.start_time, self.end_date, self.end_time))
