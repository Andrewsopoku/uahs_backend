from django.db import models

from core.models.ambulance_service import AmbulanceService
from core.models.auth_user_demographic import AuthUserDemographic
from core.models.base_model import BaseModel
from core.models.health_service import HealthService


class HealthServiceAdmin(models.Model):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE, null=True)
    health_service = models.ForeignKey(HealthService,on_delete=models.CASCADE, null=True)
