# Generated by Django 2.1.7 on 2019-08-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_ambulancerate'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='last_known_lat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='last_known_long',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
