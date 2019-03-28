from core.models.base_model import BaseModel
from django.contrib.auth.models import User, Group
from django.db import models
from datetime import date
# Create your models here.
from uahs_backend import settings

sex = (("Male", "MALE"), ("Female", "FEMALE"))
marital = (("Married", "MARRIED"), ("Single", "SINGLE"))

class AuthUserDemographic(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    title = models.CharField(max_length= 30,null=True)
    first_name = models.CharField(max_length=255,null=True)
    other_name = models.CharField(max_length=255,null=True)
    unique_id = models.CharField(max_length=255,null=True)
    surname = models.CharField(max_length=255,null=True,verbose_name="Surname")
    sex = models.CharField(max_length=255,choices=sex,verbose_name="Gender",default="Male")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    nationality = models.CharField(max_length=255,null=True)
    religion = models.CharField(max_length=255,null=True)
    marital_status = models.CharField(max_length=255,choices=marital,default="Single")
    address = models.CharField(max_length=255,null=True)
    occupation = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    country_code = models.CharField(max_length=255,null=True)
    mobile = models.CharField(max_length=255,null=True)
    emergency_contact_name = models.CharField(max_length=255,null=True)
    emergency_contact_mobile = models.CharField(max_length=255,null=True)
    emergency_contact_address = models.CharField(max_length=255, null=True)
    emergency_contact_relationship = models.CharField(max_length=255, null=True)
    first_login = models.BooleanField(default=True)

    #
    # def __str__(self):
    #     return '{} {} {}'.format(self.first_name, self.other_name, self.surname)
    #
    # def is_patient(self, ):
    #     users_in_group = Group.objects.get(name="Patient").user_set.all()
    #     return True if self.user in users_in_group else False
    #
    # def is_doctor(self, ):
    #     users_in_group = Group.objects.get(name="Doctor").user_set.all()
    #     return True if self.user in users_in_group else False
    #
    # def is_nurse(self, ):
    #     users_in_group = Group.objects.get(name="Nurse").user_set.all()
    #     return True if self.user in users_in_group else False
    #
    # def is_generalsupervisor(self, ):
    #     users_in_group = Group.objects.get(name="General Supervisor").user_set.all()
    #     return True if self.user in users_in_group else False


    def get_age(self):
        born = self.date_of_birth
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.picture.url)





