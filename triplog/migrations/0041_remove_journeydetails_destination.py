# Generated by Django 3.1 on 2020-10-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0040_auto_20201023_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journeydetails',
            name='destination',
        ),
    ]
