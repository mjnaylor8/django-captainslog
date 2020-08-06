# Generated by Django 3.0.8 on 2020-08-05 14:15

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journey_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('weather', models.CharField(max_length=256)),
                ('travel_from', models.CharField(max_length=256)),
                ('travel_to', models.CharField(max_length=256)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('duration', models.TimeField()),
                ('mileage_start', models.FloatField()),
                ('mileage_end', models.FloatField()),
                ('distance', models.FloatField()),
                ('toll_charges', models.FloatField()),
                ('toll_currency', models.CharField(max_length=3)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now_add=True)),
                ('destination', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('star_rating', models.CharField(max_length=256)),
                ('would_return', models.BooleanField()),
                ('notes', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Site_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address_line1', models.CharField(max_length=256)),
                ('address_line2', models.CharField(max_length=256)),
                ('address_line3', models.CharField(max_length=256)),
                ('address_code', models.CharField(max_length=256)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('email', models.CharField(max_length=256)),
                ('phone_number', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Site_Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greeting', models.CharField(max_length=256)),
                ('pitch_type', models.CharField(max_length=256)),
                ('pitch_level', models.CharField(max_length=256)),
                ('hook_up', models.CharField(max_length=256)),
                ('waste', models.CharField(max_length=256)),
                ('toilets', models.CharField(max_length=256)),
                ('ambience', models.CharField(max_length=256)),
                ('security', models.CharField(max_length=256)),
                ('wifi', models.CharField(max_length=256)),
                ('tv_signal', models.CharField(max_length=256)),
                ('phone_signal_3G_4G', models.CharField(max_length=256)),
                ('pets', models.CharField(max_length=256)),
                ('children', models.CharField(max_length=256)),
                ('laundry', models.CharField(max_length=256)),
                ('cost_charges', models.FloatField()),
                ('cost_extras', models.FloatField()),
                ('cost_currency', models.CharField(max_length=3)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triplog.Site_Information')),
            ],
        ),
    ]
