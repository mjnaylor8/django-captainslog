# Generated by Django 3.1 on 2020-10-23 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0038_auto_20201023_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydetails',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='journey_destination', to='triplog.siteinformation'),
        ),
        migrations.AlterField(
            model_name='journeydetails',
            name='travel_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='journey_from', to='triplog.siteinformation'),
        ),
        migrations.AlterField(
            model_name='journeydetails',
            name='travel_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='journey_to', to='triplog.siteinformation'),
        ),
    ]
