# Generated by Django 3.1 on 2020-08-25 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('triplog', '0011_auto_20200816_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteinformation',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='ambience',
            field=models.CharField(blank=True, choices=[('Peaceful', 'Peaceful'), ('OK', 'OK'), ('Loud / Lively', 'Loud / Lively')], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='children',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='cost_charges',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='cost_currency',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='cost_extras',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='edited_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='greeting',
            field=models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Indifferent', 'Indifferent')], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='hook_up',
            field=models.CharField(blank=True, choices=[('6A', '6A'), ('10A', '10A'), ('16A', '16A')], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='laundry',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='pets',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='phone_signal_3G_4G',
            field=models.CharField(blank=True, choices=[('Good', 'Good'), ('Poor', 'Poor')], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='pitch_level',
            field=models.CharField(blank=True, choices=[('Level', 'Level'), ('Gentle Slope', 'Gentle Slope'), ('Steep Slope', 'Steep Slope'), ('Impossible Slope', 'Impossible Slope')], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='pitch_type',
            field=models.CharField(blank=True, choices=[('Level', 'Level'), ('Gentle Slope', 'Gentle Slope'), ('Steep Slope', 'Steep Slope'), ('Impossible Slope', 'Impossible Slope')], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='security',
            field=models.CharField(blank=True, choices=[('Good', 'Good'), ('Poor', 'Poor')], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='toilets',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Clean', 'Clean'), ('Dirty', 'Dirty'), ("Don't Go There", "Don't Go There")], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='tv_signal',
            field=models.CharField(blank=True, choices=[('Good', 'Good'), ('Poor', 'Poor')], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='waste',
            field=models.CharField(blank=True, choices=[('On Pitch', 'On Pitch'), ('Close By', 'Close By'), ('Miles Away', 'Miles Away')], max_length=256),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='wifi',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='journeydetails',
            name='star_rating',
            field=models.CharField(max_length=256),
        ),
        migrations.DeleteModel(
            name='SiteFacilities',
        ),
    ]
