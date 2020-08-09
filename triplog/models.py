from django.db import models
from django.contrib.gis.db import models
from mapbox_location_field.spatial.models import SpatialLocationField
from mapbox_location_field.models import AddressAutoHiddenField

# Create your models here.

class Site_Information(models.Model):
    name = models.CharField(max_length=256)
    address = AddressAutoHiddenField(null=True)
    email = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=256)
    location = SpatialLocationField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Journey_Details(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    weather = models.CharField(max_length=256)
    travel_from = models.CharField(max_length=256)
    travel_to = models.CharField(max_length=256)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.TimeField()
    mileage_start = models.FloatField()
    mileage_end = models.FloatField()
    distance = models.FloatField()
    toll_charges = models.FloatField()
    toll_currency = models.CharField(max_length=3)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now_add=True)
    star_rating = models.CharField(max_length=256)
    would_return = models.BooleanField()
    notes = models.CharField(max_length=1024)
    destination = models.ForeignKey(Site_Information, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str('%s - %s - %s - %s' % (self.start_date, self.start_time, self.end_date, self.end_time))

class Site_Facilities(models.Model):
    name = models.ForeignKey(Site_Information, on_delete=models.CASCADE)
    greeting = models.CharField(max_length=256)
    pitch_type = models.CharField(max_length=256)
    pitch_level = models.CharField(max_length=256)
    hook_up = models.CharField(max_length=256)
    waste = models.CharField(max_length=256)
    toilets = models.CharField(max_length=256)
    ambience = models.CharField(max_length=256)
    security  = models.CharField(max_length=256)
    wifi = models.CharField(max_length=256)
    tv_signal  = models.CharField(max_length=256)
    phone_signal_3G_4G = models.CharField(max_length=256)
    pets = models.CharField(max_length=256)
    children = models.CharField(max_length=256)
    laundry = models.CharField(max_length=256)
    cost_charges = models.FloatField()
    cost_extras = models.FloatField()
    cost_currency = models.CharField(max_length=3)

    def __str__(self):
        return str(self.name)