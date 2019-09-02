from django.contrib import messages
from django.shortcuts import render, redirect

from core.forms.ambulance_form import NewAmbulanceForm
from core.forms.ambulance_service_form import AssignDriverAmbulance
from core.models.ambulance import Ambulance
from core.models.ambulance_driver import AmbulanceDriver
from core.models.ambulance_driver_assignment import AmbulanceDriverAssignment
from core.models.ambulance_service import AmbulanceService



def list_driver(request,pk):
    ambulance_service = AmbulanceService.objects.get(id=pk)
    driver_list = AmbulanceDriver.objects.filter(ambulance_service=ambulance_service)
    context = {"driver_list":driver_list}
    return render(request, 'driver_list.html',context)

def assign_driver_to_ambulance(request,pk):
    ambulance_service = AmbulanceService.objects.get(id=pk)
    if request.method == "POST":
        assigndriverambulance = AssignDriverAmbulance(data=request.POST,
                                                      amb_service=ambulance_service)

        if assigndriverambulance.is_valid():

            driver = assigndriverambulance.cleaned_data['driver']
            ambulance = assigndriverambulance.cleaned_data['ambulance']
            driver_assignment = AmbulanceDriver.objects.get(id=driver)
            ambulance_assignment = Ambulance.objects.get(id=ambulance)

            assignment = AmbulanceDriverAssignment(driver=driver_assignment,
                                                   ambulance=ambulance_assignment,
                                                   ambulance_service=ambulance_service)
            assignment.save()
            messages.success(request, 'Driver Ambulance Assignment Successful')

    assigndriverambulance = AssignDriverAmbulance(amb_service=ambulance_service)
    assignments = AmbulanceDriverAssignment.objects.filter(
        ambulance_service=ambulance_service)
    context = {'assigndriverambulance':assigndriverambulance,'assignments':assignments}
    return render(request,'driver_to_ambulance_assignment.html',context)

def change_driver_status(request,driver_pk,new_status):
    driver = AmbulanceDriver.objects.get(id = driver_pk)
    if driver:
        driver.status = new_status
        driver.save()

    return redirect(request.META['HTTP_REFERER'])
