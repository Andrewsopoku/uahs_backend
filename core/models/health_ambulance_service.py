from django.db import models

from core.models.ambulance_service import AmbulanceService
from core.models.health_service import HealthService


class HealthAmbulanceService(models.Model):
    health_service = models.ForeignKey(HealthService, on_delete=models.CASCADE, null=True)
    ambulance_service = models.ForeignKey(AmbulanceService,on_delete=models.CASCADE, null=True)
