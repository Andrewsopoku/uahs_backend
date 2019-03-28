from django.db import models

from core.models.ambulance_service import AmbulanceService
from core.models.auth_user_demographic import AuthUserDemographic
from core.models.base_model import BaseModel

class AmbulanceServiceAdmin(models.Model):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE, null=True)
    ambulance_service = models.ForeignKey(AmbulanceService,on_delete=models.CASCADE, null=True)
