""" Defines Models """
import os
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}/{2}'.format('routes', str(instance.user.id).zfill(2), filename)

# Sites
class Sites(models.Model):
    site_latitude = models.FloatField()
    site_longitude = models.FloatField()
    site_name = models.CharField(max_length=256)
    mpoly = models.PointField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.site_name

# Overwrite name
class OverwriteStorage(FileSystemStorage):
    # Allow the file to be saved as the same name i.e. overwritten
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

# GeoJSON Route
class GeoJSONRoute(models.Model):
    route_file = models.FileField(upload_to=user_directory_path, null=True, \
        storage=OverwriteStorage)
    route_description = models.CharField(max_length=256)
    route_name = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, \
        blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.route_name)
