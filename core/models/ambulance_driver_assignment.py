from core.models.ambulance import Ambulance
from core.models.ambulance_driver import AmbulanceDriver
from core.models.ambulance_service import AmbulanceService
from core.models.base_model import BaseModel
from django.db import models


class AmbulanceDriverAssignment(BaseModel):
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(AmbulanceDriver, on_delete=models.CASCADE, null=True)
    ambulance_service = models.ForeignKey(AmbulanceService,on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=255, null=True, default= "Active")

