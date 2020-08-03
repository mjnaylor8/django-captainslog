from django.db import models
from djgeojson.fields import PointField

# Create your models here.

class sites(models.Model):
    site_latitude = models.FloatField()
    site_longitude = models.FloatField()
    site_name = models.CharField(max_length=256)
    mpoly = PointField()

      # Returns the string representation of the model.
    def __str__(self):
        return self.site_name