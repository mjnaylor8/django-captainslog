# Generated by Django 3.1 on 2020-11-19 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripdetail',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
