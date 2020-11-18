# Generated by Django 3.1 on 2020-10-22 20:05

from django.db import migrations, models
import django.utils.timezone
import triplog.models


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0027_auto_20201022_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydetail',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='journeydetail',
            name='edited_date',
            field=models.DateTimeField(verbose_name=triplog.models.AutoDateTimeField(default=django.utils.timezone.now)),
        ),
        migrations.AlterField(
            model_name='siteinformation',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='siteinformation',
            name='edited_date',
            field=models.DateTimeField(verbose_name=triplog.models.AutoDateTimeField(default=django.utils.timezone.now)),
        ),
    ]