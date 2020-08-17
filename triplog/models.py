from django.contrib.gis.db import models
from mapbox_location_field.spatial.models import SpatialLocationField
from mapbox_location_field.models import AddressAutoHiddenField

# Create your models here.

class SITEINFORMATION(models.Model):
    name = models.CharField(max_length=256)
    address = AddressAutoHiddenField()
    email = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=256, blank=True)
    location = SpatialLocationField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class JOURNEYDETAILS(models.Model):
    true_false_choices = [
        (True, "Yes"),
        (False, "No")
    ]
    ONESTAR = '*'
    TWOSTAR = '**'
    THREESTAR = '***'
    FOURSTAR = '****'
    FIVESTAR = '*****'
    STAR_RATING_CHOICES = [
        (ONESTAR, "One Star"),
        (TWOSTAR, "Two Star"),
        (THREESTAR, "Three Star"),
        (FOURSTAR, "Four Star"),
        (FIVESTAR, "Five Star"),
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
    would_return = models.BooleanField(blank=True, choices=true_false_choices, null=True)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    destination = models.ForeignKey(SITEINFORMATION, models.SET_NULL, null=True)

    def __str__(self):
        return str('%s - %s - %s - %s' % (self.start_date, self.start_time, self.end_date, self.end_time))

class SITEFACILITIES(models.Model):
    excellent = "Excellent"
    good = "Good"
    indifferent = "Indifferent"
    dirt = "dirt"
    grass = "grass"
    hardstanding = "Hardstanding"
    level = "Level"
    gentle_slope = "Gentle Slope"
    steep_slope = "Steep Slope"
    impossible_slope = "Impossible Slope"
    six_amp = "6A"
    ten_amp = "10A"
    sixteen_amp = "16A"
    on_pitch = "On Pitch"
    close_by = "Close By"
    miles_away = "Miles Away"
    none = "None"
    clean = "Clean"
    dirty = "Dirty"
    dont_go_there = "Don't Go There"
    peaceful = "Peaceful"
    okay = "OK"
    loud_lively = "Loud / Lively"
    poor = "Poor"
    greeting_choices = [
        (excellent, "Excellent"),
        (good, "Good"),
        (indifferent, "Indifferent"),
    ]
    pitch_type_choices = [
        (dirt, "Dirt"),
        (grass, "Grass"),
        (hardstanding, "Hardstanding"),
    ]
    pitch_levels_choices = [
        (level, "Level"),
        (gentle_slope, "Gentle Slope"),
        (steep_slope, "Steep Slope"),
        (impossible_slope, "Impossible Slope"),
    ]
    hook_up_choices = [
        (six_amp, "6A"),
        (ten_amp, "10A"),
        (sixteen_amp, "16A"),
    ]

    waste_choices = [
        (on_pitch, "On Pitch"),
        (close_by, "Close By"),
        (miles_away, "Miles Away"),
    ]

    toilet_choices = [
        (none, "None"),
        (clean, "Clean"),
        (dirty, "Dirty"),
        (dont_go_there, "Don't Go There"),
    ]

    ambience_choices = [
        (peaceful, "Peaceful"),
        (okay, "OK"),
        (loud_lively, "Loud / Lively"),
    ]

    security_choices = [
        (good, "Good"),
        (poor, "Poor"),
    ]

    tv_signal_choices = [
        (good, "Good"),
        (poor, "Poor"),
    ]
    phone_signal_3G_4G_choices = [
        (good, "Good"),
        (poor, "Poor"),
    ]

    true_false_choices = [
        (True, "Yes"),
        (False, "No")
    ]
    name = models.ForeignKey(SITEINFORMATION, on_delete=models.CASCADE)
    greeting = models.CharField(max_length=256, blank=True, choices=greeting_choices)
    pitch_type = models.CharField(max_length=256, blank=True, choices=pitch_levels_choices)
    pitch_level = models.CharField(max_length=256, blank=True, choices=pitch_levels_choices)
    hook_up = models.CharField(max_length=256, blank=True, choices=hook_up_choices)
    waste = models.CharField(max_length=256, blank=True, choices=waste_choices)
    toilets = models.CharField(max_length=256, blank=True, choices=toilet_choices)
    ambience = models.CharField(max_length=256, blank=True, choices=ambience_choices)
    security = models.CharField(max_length=256, blank=True, choices=security_choices)
    wifi = models.BooleanField(blank=True, choices=true_false_choices)
    tv_signal = models.CharField(max_length=256, blank=True, choices=tv_signal_choices)
    phone_signal_3G_4G = models.CharField(max_length=256, blank=True, choices=phone_signal_3G_4G_choices)
    pets = models.BooleanField(blank=True, choices=true_false_choices)
    children = models.BooleanField(blank=True, choices=true_false_choices)
    laundry = models.BooleanField(blank=True, choices=true_false_choices)
    cost_charges = models.FloatField(blank=True)
    cost_extras = models.FloatField(blank=True)
    cost_currency = models.CharField(max_length=3, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
