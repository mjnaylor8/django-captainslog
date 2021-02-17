# Generated by Django 3.1 on 2020-11-28 19:16

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0003_auto_20201122_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinformation',
            name='country',
            field=mapbox_location_field.models.AddressCountryField(blank=True, map_id='map', null=True),
        ),
    ]