from core.core_util import get_area
from core.models.ambulance import Ambulance
from core.models.ambulance_service import AmbulanceService
from core.models.auth_user_demographic import AuthUserDemographic
from core.models.base_model import BaseModel, get_object_or_none
from django.db import models

class Transaction(BaseModel):
    init_from_lat = models.CharField(max_length=255, null=True)
    init_to_lat = models.CharField(max_length=255, null=True)
    init_from_long = models.CharField(max_length=255, null=True)
    init_to_long = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    init_distance = models.CharField(max_length= 255,null=True)
    final_distance = models.CharField(max_length=255, null=True)
    final_from_lat = models.CharField(max_length=255, null=True)
    final_to_lat = models.CharField(max_length=255, null=True)
    final_from_long = models.CharField(max_length=255, null=True)
    final_to_long = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    init_charge = models.CharField(max_length=255, null=True)
    final_charge = models.CharField(max_length=255, null=True)
    patient = models.ForeignKey(AuthUserDemographic, related_name= "patient",
                                on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(AuthUserDemographic,related_name="driver",
                               on_delete=models.CASCADE, null=True)
    ambulance = models.ForeignKey(Ambulance, related_name = "ambulance",
                                  on_delete=models.CASCADE, null=True)


    @classmethod
    def get_order_count_for_ambulance_service(cls,ambulance_service):
        from api.views.transactions import END_TRIP
        return len([trans for trans in cls.objects.filter(status=END_TRIP).exclude(ambulance__isnull=True) if trans.ambulance.ambulance_service == ambulance_service ])

    @classmethod
    def get_trips_for_ambulance_service(cls, ambulance_service):
        from api.views.transactions import END_TRIP
        return [trans for trans in cls.objects.filter(status=END_TRIP).exclude(ambulance__isnull=True) if
                    trans.ambulance.ambulance_service == ambulance_service]

    def get_from_address(self):
        return get_area(self.final_from_lat,self.final_from_long)

    def get_to_address(self):
        return get_area(self.final_to_lat,self.final_to_long)
