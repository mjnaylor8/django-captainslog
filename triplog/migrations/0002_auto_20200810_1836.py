# Generated by Django 3.1 on 2020-08-10 18:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mapbox_location_field.models
import mapbox_location_field.spatial.models


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey_details',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='triplog.site_information'),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='distance',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='duration',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='end_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='mileage_end',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='star_rating',
            field=models.CharField(choices=[('*', 'One Star'), ('**', 'Two Star'), ('***', 'Three Star'), ('****', 'Four Star'), ('*****', 'Five Star')], max_length=256),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='start_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='toll_charges',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='toll_currency',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='travel_to',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='journey_details',
            name='weather',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='ambience',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='children',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='cost_charges',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='cost_currency',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='cost_extras',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='greeting',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='hook_up',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='laundry',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='pets',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='phone_signal_3G_4G',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='pitch_level',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='pitch_type',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='security',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='toilets',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='tv_signal',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='waste',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_facilities',
            name='wifi',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_information',
            name='address',
            field=mapbox_location_field.models.AddressAutoHiddenField(default='home', map_id='map'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site_information',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site_information',
            name='email',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='site_information',
            name='location',
            field=mapbox_location_field.spatial.models.SpatialLocationField(blank=True, map_attrs={}, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='site_information',
            name='phone_number',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]