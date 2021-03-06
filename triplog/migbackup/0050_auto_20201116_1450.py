# Generated by Django 3.1 on 2020-11-16 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0049_auto_20201116_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripdetails',
            name='journeys',
        ),
        migrations.AddField(
            model_name='journeydetail',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip', to='triplog.tripdetails'),
        ),
        migrations.AddField(
            model_name='tripdetails',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
