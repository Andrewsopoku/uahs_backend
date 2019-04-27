from countries_plus.models import Country
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from core.forms.health_service_form import NewHealthServiceForm
from core.models.ambulance_service import AmbulanceService
from core.models.contact_person import ContactPerson
from core.models.health_ambulance_service import HealthAmbulanceService
from core.models.health_service import HealthService
from core.models.physical_address import PhysicalAddress


def add_new_health_service(request):

    if request.method == "POST":
        new_health_service_form = NewHealthServiceForm(request.POST)
        if new_health_service_form.is_valid():
            name = new_health_service_form.cleaned_data['name']
            country = new_health_service_form.cleaned_data['country']
            area_of_operation = new_health_service_form.cleaned_data['area_of_operation']
            email = new_health_service_form.cleaned_data['email']
            mobile = new_health_service_form.cleaned_data['mobile']
            region = new_health_service_form.cleaned_data['region']
            town = new_health_service_form.cleaned_data['town']
            gps_long = new_health_service_form.cleaned_data['gps_long']
            gps_lat = new_health_service_form.cleaned_data['gps_long']
            has_ambulance = new_health_service_form.cleaned_data['has_ambulance']

            contact_person_first_name = new_health_service_form.cleaned_data['contact_person_first_name']
            contact_person_last_name = new_health_service_form.cleaned_data['contact_person_last_name']
            contact_person_address = new_health_service_form.cleaned_data['contact_person_address']
            contact_person_phone_number = new_health_service_form.cleaned_data['contact_person_phone_number']
            contact_person_email = new_health_service_form.cleaned_data['contact_person_email']

            country_code = Country.objects.get(iso_numeric=country).phone
            country_name = Country.objects.get(iso_numeric=country).name

            contact_person = ContactPerson(first_name=contact_person_first_name ,last_name=contact_person_last_name,
                                           phone_number=contact_person_phone_number ,address=contact_person_address,
                                           email=contact_person_email)
            contact_person.save()

            physical_address = PhysicalAddress(country=country_name ,region=region ,town=town ,gps_long=gps_long,
                                               gps_lat=gps_lat)
            physical_address.save()

            health_service = HealthService(name=name ,area_of_operation=area_of_operation ,email=email ,mobile=mobile
                             ,country_code=country_code,
                             physical_address=physical_address ,contact_person=contact_person)
            health_service.save()
            if has_ambulance:
                ambulance_service = AmbulanceService(name=name, area_of_operation=area_of_operation, email=email, mobile=mobile
                              , country_code=country_code,is_for_health_service=True,
                              physical_address=physical_address, contact_person=contact_person)
                ambulance_service.save()
                HealthAmbulanceService(health_service=health_service,ambulance_service=ambulance_service).save()

            messages.success(request, "Health Service Added Successfully")

        else:
            context = {'new_health_service_form': new_health_service_form}
            return render(request, 'add_ambulance_service.html', context)

    new_health_service_form = NewHealthServiceForm()
    context = { 'new_health_service_form': new_health_service_form}
    return render(request, 'new_health_service.html', context)

def view_health_services(request):
    health_services = HealthService.objects.all()
    context = {"health_services":health_services}
    return render(request, 'view_health_service.html', context)

def add_ambulance_service_to_health_service(request,pk):
    health_service = HealthService.objects.get(id=pk)
    if health_service.get_ambulance_service():
        messages.error(request,"Health Service already has Ambulance service")
    else:
        ambulance_service = AmbulanceService(name=health_service.name,
                                             area_of_operation=health_service.area_of_operation,
                                             email=health_service.email,
                                             mobile=health_service.mobile,
                                             country_code=health_service.country_code,
                                             is_for_health_service=True,
                                             physical_address=health_service.physical_address,
                                             contact_person=health_service.contact_person)

        ambulance_service.save()
        HealthAmbulanceService(health_service=health_service, ambulance_service=ambulance_service).save()

        messages.success(request, "Ambulance service added to Health Service")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
