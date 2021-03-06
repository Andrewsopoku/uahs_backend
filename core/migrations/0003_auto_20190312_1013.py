# Generated by Django 2.1.7 on 2019-03-12 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190227_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('picture', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('registration_number', models.CharField(max_length=255, null=True)),
                ('dominant_color', models.CharField(max_length=255, null=True)),
                ('make_year', models.CharField(max_length=255, null=True)),
                ('model', models.CharField(max_length=255, null=True)),
                ('is_for_ambulance_service', models.BooleanField(default=True)),
                ('is_for_health_service', models.BooleanField(default=False)),
                ('ambulance_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AmbulanceService')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AmbulanceServiceAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ambulance_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AmbulanceService')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('logo', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('name', models.CharField(max_length=255, null=True)),
                ('country_code', models.CharField(max_length=255, null=True)),
                ('mobile', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('area_of_operation', models.CharField(max_length=255, null=True)),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ContactPerson')),
                ('physical_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PhysicalAddress')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ambulance',
            name='health_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.HealthService'),
        ),
    ]
