from django.contrib import messages
from django.shortcuts import render

from core.forms.ambulance_form import NewAmbulanceForm
from core.models.ambulance import Ambulance
from core.models.ambulance_driver import AmbulanceDriver
from core.models.ambulance_service import AmbulanceService



def list_driver(request,pk):
    ambulance_service = AmbulanceService.objects.get(id=pk)
    driver_list = AmbulanceDriver.objects.filter(ambulance_service=ambulance_service)
    context = {"driver_list":driver_list}
    return render(request, 'driver_list.html',context)
