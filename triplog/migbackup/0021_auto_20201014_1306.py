# Generated by Django 3.1 on 2020-10-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0020_auto_20201014_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinformation',
            name='star_rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
