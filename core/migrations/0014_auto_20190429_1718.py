# Generated by Django 2.1.7 on 2019-04-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190429_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuserdemographic',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
    ]
