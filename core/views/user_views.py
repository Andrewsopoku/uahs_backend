import datetime
import random
from urllib import request

import requests
from countries_plus.models import Country
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render

from core.core_util import add_zeros, randomPassword
from core.forms.user_form import NewAmbulanceServiceForm, NewAmbulanceServiceAdminForm, NewAmbulanceDriverForm, \
    NewHealthServiceAdminForm
from core.models.ambulance_driver import AmbulanceDriver
from core.models.ambulance_service import AmbulanceService
from core.models.ambulance_service_admin import AmbulanceServiceAdmin
from core.models.auth_user_demographic import AuthUserDemographic
from core.models.contact_person import ContactPerson
from core.models.health_service import HealthService
from core.models.health_service_admin import HealthServiceAdmin
from core.models.physical_address import PhysicalAddress



def sendsms(request,contact,pin):
    url = "http://sms.nasaramobile.com/api/v2/sendsms"

    response = requests.get( url="http://sms.nasaramobile.com/api?"
                                    "api_key=5bc2dfb823e475bc2dfb823e88&&sender_id=Yaresa"
                                    "&&phone="+str(contact)+"&&message=Thanks for registering for UAHS services. "
                                 "Download UAHS app at .Your temporal pin is "+str(pin))
    print(response)
    print(response.reason)
    print(response.content)

def add_new_ambulance_service(request):

        if request.method == "POST":
            new_ambulance_service_form = NewAmbulanceServiceForm(request.POST)
            if new_ambulance_service_form.is_valid():
                name = new_ambulance_service_form.cleaned_data['name']
                country = new_ambulance_service_form.cleaned_data['country']
                area_of_operation = new_ambulance_service_form.cleaned_data['area_of_operation']
                email = new_ambulance_service_form.cleaned_data['email']
                mobile = new_ambulance_service_form.cleaned_data['mobile']
                region = new_ambulance_service_form.cleaned_data['region']
                town = new_ambulance_service_form.cleaned_data['town']
                gps_long = new_ambulance_service_form.cleaned_data['gps_long']
                gps_lat = new_ambulance_service_form.cleaned_data['gps_long']

                contact_person_first_name = new_ambulance_service_form.cleaned_data['contact_person_first_name']
                contact_person_last_name = new_ambulance_service_form.cleaned_data['contact_person_last_name']
                contact_person_address = new_ambulance_service_form.cleaned_data['contact_person_address']
                contact_person_phone_number = new_ambulance_service_form.cleaned_data['contact_person_phone_number']
                contact_person_email = new_ambulance_service_form.cleaned_data['contact_person_email']

                country_code = Country.objects.get(iso_numeric=country).phone
                country_name = Country.objects.get(iso_numeric=country).name

                contact_person = ContactPerson(first_name=contact_person_first_name,last_name=contact_person_last_name,
                                               phone_number=contact_person_phone_number,address=contact_person_address,
                                               email=contact_person_email)
                contact_person.save()

                physical_address = PhysicalAddress(country=country_name,region=region,town=town,gps_long=gps_long,
                                                   gps_lat=gps_lat)
                physical_address.save()

                AmbulanceService(name=name,area_of_operation=area_of_operation,email=email,mobile=mobile,country_code=country_code,
                                 physical_address=physical_address,contact_person=contact_person).save()

                messages.success(request, "Ambulance Service Added Successfully")

            else:
                context = {'new_ambulance_service_form': new_ambulance_service_form}
                return render(request, 'add_ambulance_service.html', context)

        new_ambulance_service_form = NewAmbulanceServiceForm()
        context = { 'new_ambulance_service_form': new_ambulance_service_form}
        return render(request, 'add_ambulance_service.html', context)


def view_ambulance_services(request):
    ambulance_services = AmbulanceService.objects.all()
    context = {"ambulance_services":ambulance_services}
    return render(request, 'view_ambulance_service.html', context)


def add_ambulance_service_admin(request,pk):
    if request.method == "POST":
        new_ambulance_service_admin_form = NewAmbulanceServiceAdminForm(request.POST)
        if new_ambulance_service_admin_form.is_valid():
            firstname = new_ambulance_service_admin_form.cleaned_data['first_name']
            nationality = new_ambulance_service_admin_form .cleaned_data['nationality']
            surname = new_ambulance_service_admin_form .cleaned_data['surname']

            mobile = new_ambulance_service_admin_form .cleaned_data['mobile']
            email = new_ambulance_service_admin_form .cleaned_data['email']
            address = new_ambulance_service_admin_form .cleaned_data['address']
            dob = new_ambulance_service_admin_form .cleaned_data['date_of_birth']
            sex = new_ambulance_service_admin_form .cleaned_data['sex']

            pin = random.randint(1000, 9999)
            unique_id = "1"

            now = datetime.datetime.now()

            try:
                user = User.objects.create_user(username=email, password=pin,)
                user.groups.add(Group.objects.get_or_create(name="Ambulance Admin")[0])
                user.save()
            except Exception as ab:
                messages.error(request, ab)

            else:

                user_info = AuthUserDemographic(user=user, email=email,
                                                    first_name=firstname,
                                                    surname=surname, sex=sex, date_of_birth=dob,
                                                    nationality=nationality,
                                                    address=address,
                                                    mobile=mobile )

                user_info.save()

                user_info.unique_id = '{}{}{}{}'.format(now.day, now.month,
                                                            now.year, add_zeros(5, str(user_info.id)))

                user_info.save()
                ambulance_service = AmbulanceService.objects.get(id=pk)
                absa = AmbulanceServiceAdmin(user=user_info, ambulance_service=ambulance_service)
                absa.save()
                sendsms(request, mobile, pin)

                messages.success(request, "Ambulance Service Admin Added Successfully")

        else:
            context = {'new_ambulance_service_admin_form ': new_ambulance_service_admin_form }
            return render(request, 'add_ambulance_service.html', context)

    new_ambulance_service_admin_form = NewAmbulanceServiceAdminForm()

    context = {'new_ambulance_service_admin_form': new_ambulance_service_admin_form }
    return render(request, 'ambulance_service_admin.html', context)


def add_ambulance_driver(request,pk):
    if request.method == "POST":
        new_ambulance_driver_form = NewAmbulanceDriverForm(request.POST)
        if new_ambulance_driver_form.is_valid():
            firstname = new_ambulance_driver_form.cleaned_data['first_name']
            nationality = new_ambulance_driver_form .cleaned_data['nationality']
            surname = new_ambulance_driver_form .cleaned_data['surname']

            mobile = new_ambulance_driver_form .cleaned_data['mobile']
            email = new_ambulance_driver_form .cleaned_data['email']
            address = new_ambulance_driver_form .cleaned_data['address']
            dob = new_ambulance_driver_form .cleaned_data['date_of_birth']
            sex = new_ambulance_driver_form .cleaned_data['sex']
            driver_license_number = new_ambulance_driver_form .cleaned_data['driver_license_number']
            password = randomPassword()

            print(password)
            now = datetime.datetime.now()

            try:
                user = User.objects.create_user(username=email, password=password,)
                user.groups.add(Group.objects.get_or_create(name="Ambulance Driver")[0])
                user.save()
            except Exception as ab:
                messages.error(request, ab)

            else:

                user_info = AuthUserDemographic(user=user, email=email,
                                                    first_name=firstname,
                                                    surname=surname, sex=sex, date_of_birth=dob,
                                                    nationality=nationality,
                                                    address=address,
                                                    mobile=mobile )

                user_info.save()

                user_info.unique_id = '{}{}{}{}'.format(now.day, now.month,
                                                            now.year, add_zeros(5, str(user_info.id)))

                user_info.save()
                ambulance_service = AmbulanceService.objects.get(id=pk)

                absa = AmbulanceDriver(user=user_info,driver_license_number=driver_license_number,
                                       ambulance_service= ambulance_service)
                absa.save()
                #sendsms(request, mobile, pin)

                messages.success(request, "Ambulance Driver Added Successfully")

        else:
            context = {'new_ambulance_driver_form': new_ambulance_driver_form }
            return render(request, 'add_ambulance_driver.html', context)

    new_ambulance_driver_form = NewAmbulanceDriverForm()

    context = {'new_ambulance_driver_form': new_ambulance_driver_form }
    return render(request, 'add_ambulance_driver.html', context)


def add_health_service_admin(request, pk):
    if request.method == "POST":
        new_health_service_admin_form = NewHealthServiceAdminForm(request.POST)
        if new_health_service_admin_form.is_valid():
            firstname = new_health_service_admin_form.cleaned_data['first_name']
            nationality = new_health_service_admin_form.cleaned_data['nationality']
            surname = new_health_service_admin_form.cleaned_data['surname']

            mobile = new_health_service_admin_form.cleaned_data['mobile']
            email = new_health_service_admin_form.cleaned_data['email']
            address = new_health_service_admin_form.cleaned_data['address']
            dob = new_health_service_admin_form.cleaned_data['date_of_birth']
            sex = new_health_service_admin_form.cleaned_data['sex']

            pin = random.randint(1000, 9999)
            unique_id = "1"

            now = datetime.datetime.now()

            try:
                user = User.objects.create_user(username=email, password=pin, )
                user.groups.add(Group.objects.get_or_create(name="Health Service Admin")[0])
                user.save()
            except Exception as ab:
                messages.error(request, ab)

            else:

                user_info = AuthUserDemographic(user=user, email=email,
                                                first_name=firstname,
                                                surname=surname, sex=sex, date_of_birth=dob,
                                                nationality=nationality,
                                                address=address,
                                                mobile=mobile)

                user_info.save()

                user_info.unique_id = '{}{}{}{}'.format(now.day, now.month,
                                                        now.year, add_zeros(5, str(user_info.id)))

                user_info.save()
                health_service = HealthService.objects.get(id=pk)
                hsa = HealthServiceAdmin(user=user_info, health_service=health_service)
                hsa.save()
                sendsms(request, mobile, pin)


                messages.success(request, "Health Service Admin Added Successfully")

        else:
            context = {'new_health_service_admin_form ': new_health_service_admin_form}
            return render(request, 'add_health_service.html', context)

    new_health_service_admin_form = NewHealthServiceAdminForm()

    context = {'new_health_service_admin_form': new_health_service_admin_form}

    return render(request, 'add_health_service_admin.html', context)

