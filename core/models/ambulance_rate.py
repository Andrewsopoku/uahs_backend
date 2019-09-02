from core.models.ambulance_service import AmbulanceService
from core.models.base_model import BaseModel
from django.db import models

from core.models.health_service import HealthService

class AmbulanceRate(BaseModel):

    city = models.CharField(max_length=255, null=True)
    minumum_rate = models.CharField(max_length=255, null=True)
    minumum_distance = models.CharField(max_length=255, null=True)
    rate_per_minumum_distance = models.CharField(max_length= 255,null=True)
    distance_unit = models.CharField(max_length=255, null=True,default="Metre")
    status = models.CharField(max_length=255, null=True, default= "Active")

