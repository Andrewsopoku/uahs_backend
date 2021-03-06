from core.models.ambulance_service import AmbulanceService
from core.models.base_model import BaseModel, get_object_or_none
from django.db import models

from core.models.health_service import HealthService
amb_type = (("Standard","Standard"),("Deluxe","Deluxe"))

class Ambulance(BaseModel):

    picture = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    registration_number = models.CharField(max_length=255, null=True)
    dominant_color = models.CharField(max_length=255, null=True)
    make_year = models.CharField(max_length= 255,null=True)
    car_model = models.CharField(max_length=255, null=True)
    is_for_ambulance_service = models.BooleanField(default=True)
    is_for_health_service = models.BooleanField(default=False)
    ambulance_service = models.ForeignKey(AmbulanceService,on_delete=models.CASCADE, blank=True,null=True)
    status = models.CharField(max_length=255, null=True, default= "Active")
    driver_assigned = models.BooleanField(default=False)
    last_known_lat = models.CharField(max_length=255, null=True, )
    last_known_long = models.CharField(max_length=255, null=True, )
    ambulance_type = models.CharField(max_length=255, null=True,choices=amb_type )

    #health_service = models.ForeignKey(HealthService,on_delete=models.CASCADE, blank=True, null=True)

    @classmethod
    def get_ambulance_with_reg_num(cls,reg_num):
        return get_object_or_none(cls,registration_number = reg_num)