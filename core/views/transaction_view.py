
from django.contrib import messages
from django.shortcuts import render, redirect

from core.forms.ambulance_form import NewAmbulanceForm
from core.forms.ambulance_service_form import AssignDriverAmbulance
from core.models.ambulance import Ambulance
from core.models.ambulance_driver import AmbulanceDriver
from core.models.ambulance_driver_assignment import AmbulanceDriverAssignment
from core.models.ambulance_service import AmbulanceService
from core.models.transaction import Transaction


def ambulance_service_trips(request):
    trips = Transaction.get_trips_for_ambulance_service(request.company)
    context = {"trips":trips}
    return render(request, 'trips_completed.html',context)

