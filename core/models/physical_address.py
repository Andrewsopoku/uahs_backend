from django.db.models import Model
from django.db import models

class PhysicalAddress(Model):
    country = models.CharField(max_length=255,null=True)
    region = models.CharField(max_length=255,null=True)
    town = models.CharField(max_length=255,null=True)
    gps_long = models.CharField(max_length=255,null=True,)
    gps_lat = models.CharField(max_length=255,null=True,)
