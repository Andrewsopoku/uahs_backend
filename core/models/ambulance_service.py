from django.db import models

from core.models.base_model import BaseModel
from core.models.contact_person import ContactPerson
from core.models.physical_address import PhysicalAddress



class AmbulanceService(BaseModel):

    logo = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    name = models.CharField(max_length= 255,null=True)
    country_code = models.CharField(max_length=255, null=True)
    mobile = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    physical_address = models.ForeignKey(PhysicalAddress, on_delete=models.CASCADE)
    area_of_operation = models.CharField(max_length=255,null=True)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    is_for_health_service = models.BooleanField(default=False)


    def get_number_of_driver(self):
        from core.models.ambulance_driver import AmbulanceDriver
        return AmbulanceDriver.objects.filter(ambulance_service=self).count()

    def get_number_of_ambulance(self):
        from core.models.ambulance import Ambulance
        return Ambulance.objects.filter(ambulance_service=self).count()

    def get_ambulance_orders_count(self):
        from core.models.transaction import Transaction
        return Transaction.get_order_count_for_ambulance_service(ambulance_service=self)

