from core.models.ambulance_service import AmbulanceService
from core.models.base_model import BaseModel
from django.db import models

from core.models.health_service import HealthService

class Ambulance(BaseModel):

    picture = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    registration_number = models.CharField(max_length=255, null=True)
    dominant_color = models.CharField(max_length=255, null=True)
    make_year = models.CharField(max_length= 255,null=True)
    car_model = models.CharField(max_length=255, null=True)
    is_for_ambulance_service = models.BooleanField(default=True)
    is_for_health_service = models.BooleanField(default=False)
    ambulance_service = models.ForeignKey(AmbulanceService,on_delete=models.CASCADE, blank=True,null=True)
    #health_service = models.ForeignKey(HealthService,on_delete=models.CASCADE, blank=True, null=True)

