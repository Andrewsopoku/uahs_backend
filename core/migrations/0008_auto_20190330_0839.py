# Generated by Django 2.1.7 on 2019-03-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190329_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulancedriver',
            name='driver_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ambulancedriver',
            name='status',
            field=models.CharField(default='Active', max_length=255, null=True),
        ),
    ]
