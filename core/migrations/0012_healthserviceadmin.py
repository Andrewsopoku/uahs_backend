# Generated by Django 2.1.7 on 2019-04-13 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190410_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthServiceAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.HealthService')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
        ),
    ]
