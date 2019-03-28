# Generated by Django 2.1.7 on 2019-03-12 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190312_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambulanceserviceadmin',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ambulanceserviceadmin',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='ambulanceserviceadmin',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic'),
        ),
    ]
