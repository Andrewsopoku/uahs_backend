# Generated by Django 2.1.7 on 2019-02-27 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUserDemographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('picture', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('title', models.CharField(max_length=30, null=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('other_name', models.CharField(max_length=255, null=True)),
                ('unique_id', models.CharField(max_length=255, null=True)),
                ('surname', models.CharField(max_length=255, null=True, verbose_name='Surname')),
                ('sex', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], default='Male', max_length=255, verbose_name='Gender')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('nationality', models.CharField(max_length=255, null=True)),
                ('religion', models.CharField(max_length=255, null=True)),
                ('marital_status', models.CharField(choices=[('Married', 'MARRIED'), ('Single', 'SINGLE')], default='Single', max_length=255)),
                ('address', models.CharField(max_length=255, null=True)),
                ('occupation', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('country_code', models.CharField(max_length=255, null=True)),
                ('mobile', models.CharField(max_length=255, null=True)),
                ('emergency_contact_name', models.CharField(max_length=255, null=True)),
                ('emergency_contact_mobile', models.CharField(max_length=255, null=True)),
                ('emergency_contact_address', models.CharField(max_length=255, null=True)),
                ('emergency_contact_relationship', models.CharField(max_length=255, null=True)),
                ('first_login', models.BooleanField(default=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
