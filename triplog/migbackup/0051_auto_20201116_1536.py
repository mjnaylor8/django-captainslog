# Generated by Django 3.1 on 2020-11-16 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0050_auto_20201116_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydetail',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trips', to='triplog.tripdetails'),
        ),
    ]