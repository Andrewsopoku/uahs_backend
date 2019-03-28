from django.db.models import Model
from django.db import models

class ContactPerson(Model):
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    phone_number = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True,)
    email = models.EmailField(max_length=255,null=True,)
