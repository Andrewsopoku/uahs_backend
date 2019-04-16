# Generated by Django 2.1.7 on 2019-04-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_ambulancedriverassignment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ambulancedriverassignment',
            old_name='user',
            new_name='driver',
        ),
        migrations.AddField(
            model_name='ambulancedriverassignment',
            name='ambulance_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AmbulanceService'),
        ),
    ]