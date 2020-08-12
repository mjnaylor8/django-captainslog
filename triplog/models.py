from django.db import models
from django.contrib.gis.db import models
from mapbox_location_field.spatial.models import SpatialLocationField
from mapbox_location_field.models import AddressAutoHiddenField

# Create your models here.

class Site_Information(models.Model):
    name = models.CharField(max_length=256)
    address = AddressAutoHiddenField()
    email = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=256, blank=True)
    location = SpatialLocationField(null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Journey_Details(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    weather = models.CharField(max_length=256, blank=True)
    travel_from = models.CharField(max_length=256)
    travel_to = models.CharField(max_length=256, blank=True)
    start_time = models.TimeField(blank = True)
    end_time = models.TimeField(blank = True)
    duration = models.TimeField(blank = True)
    mileage_start = models.FloatField()
    mileage_end = models.FloatField(blank = True)
    distance = models.FloatField(blank = True)
    toll_charges = models.FloatField(blank = True)
    toll_currency = models.CharField(max_length=3,blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now_add=True)
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
    star_rating = models.CharField(choices = STAR_RATING_CHOICES, max_length=256)

    would_return = models.BooleanField()
    notes = models.CharField(max_length=1024)
    destination = models.ForeignKey(Site_Information,models.SET_NULL,null=True)

    def __str__(self):
        return str('%s - %s - %s - %s' % (self.start_date, self.start_time, self.end_date, self.end_time))

class Site_Facilities(models.Model):
    name = models.ForeignKey(Site_Information, on_delete=models.CASCADE)
    greeting = models.CharField(max_length=256,blank = True)
    pitch_type = models.CharField(max_length=256,blank = True)
    pitch_level = models.CharField(max_length=256,blank = True)
    hook_up = models.CharField(max_length=256,blank = True)
    waste = models.CharField(max_length=256,blank = True)
    toilets = models.CharField(max_length=256,blank = True)
    ambience = models.CharField(max_length=256,blank = True)
    security  = models.CharField(max_length=256,blank = True)
    wifi = models.CharField(max_length=256,blank = True)
    tv_signal  = models.CharField(max_length=256,blank = True)
    phone_signal_3G_4G = models.CharField(max_length=256,blank = True)
    pets = models.CharField(max_length=256,blank = True)
    children = models.CharField(max_length=256,blank = True)
    laundry = models.CharField(max_length=256,blank = True)
    cost_charges = models.FloatField(blank = True)
    cost_extras = models.FloatField(blank = True)
    cost_currency = models.CharField(max_length=3,blank = True)

    def __str__(self):
        return str(self.name)