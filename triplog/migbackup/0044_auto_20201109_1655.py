# Generated by Django 3.1 on 2020-11-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0043_auto_20201105_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydetail',
            name='mileage_end',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journeydetail',
            name='mileage_start',
            field=models.IntegerField(),
        ),
    ]