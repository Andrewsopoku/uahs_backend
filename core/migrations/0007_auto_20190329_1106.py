# Generated by Django 2.1.7 on 2019-03-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_ambulance_health_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='driver_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='status',
            field=models.CharField(default='Active', max_length=255, null=True),
        ),
    ]
