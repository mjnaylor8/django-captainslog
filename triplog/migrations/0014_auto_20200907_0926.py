# Generated by Django 3.1 on 2020-09-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0013_auto_20200905_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydetails',
            name='star_rating',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
