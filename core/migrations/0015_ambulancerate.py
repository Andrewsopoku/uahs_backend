# Generated by Django 2.1.7 on 2019-06-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20190429_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmbulanceRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('minumum_rate', models.CharField(max_length=255, null=True)),
                ('minumum_distance', models.CharField(max_length=255, null=True)),
                ('rate_per_minumum_distance', models.CharField(max_length=255, null=True)),
                ('distance_unit', models.CharField(default='Metre', max_length=255, null=True)),
                ('status', models.CharField(default='Active', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
