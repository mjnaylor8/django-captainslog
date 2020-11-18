# Generated by Django 3.1 on 2020-11-15 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('triplog', '0046_author_image_tag_tripdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripdetails',
            name='journey',
        ),
        migrations.RemoveField(
            model_name='tripdetails',
            name='site',
        ),
        migrations.AddField(
            model_name='tripdetails',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tripdetails',
            name='edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_edited_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tripdetails',
            name='edited_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='TripSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitevisit', to='triplog.siteinformation')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sitevisit', to='triplog.tripdetails')),
            ],
        ),
        migrations.CreateModel(
            name='TripJourney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tripjourney', to='triplog.journeydetail')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tripjourney', to='triplog.tripdetails')),
            ],
        ),
        migrations.AddField(
            model_name='tripdetails',
            name='journeys',
            field=models.ManyToManyField(blank=True, related_name='journeys', through='triplog.TripJourney', to='triplog.JourneyDetail'),
        ),
        migrations.AddField(
            model_name='tripdetails',
            name='sites',
            field=models.ManyToManyField(blank=True, related_name='sites', through='triplog.TripSite', to='triplog.SiteInformation'),
        ),
    ]
