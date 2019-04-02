from django.contrib import messages
from django.shortcuts import render

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
            messages.success(request, 'Login successful')
            #return redirect('core:dashboard')
            #return redirect('core:dashboard')

            messages.error(request, 'Wrong username or password')

    assigndriverambulance = AssignDriverAmbulance(amb_service=ambulance_service)
    assignments = AmbulanceDriverAssignment.objects.filter(
        ambulance_service=ambulance_service)
    context = {'assigndriverambulance':assigndriverambulance,}
    return render(request,'driver_to_ambulance_assignment.html',context)

