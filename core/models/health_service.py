from django.db import models
from core.models.base_model import BaseModel
from core.models.contact_person import ContactPerson
from core.models.physical_address import PhysicalAddress


class HealthService(BaseModel):

    logo = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    name = models.CharField(max_length= 255,null=True)
    country_code = models.CharField(max_length=255, null=True)
    mobile = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    physical_address = models.ForeignKey(PhysicalAddress, on_delete=models.CASCADE)
    area_of_operation = models.CharField(max_length=255,null=True)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)

    def get_ambulance_service(self):
        from core.models.health_ambulance_service import HealthAmbulanceService

        ambulance_service = HealthAmbulanceService.objects.filter(health_service=self)
        return ambulance_service[0].ambulance_service if ambulance_service else False