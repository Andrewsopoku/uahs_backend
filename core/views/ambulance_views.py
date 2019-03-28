from django.contrib import messages
from django.shortcuts import render

from core.forms.ambulance_form import NewAmbulanceForm
from core.models.ambulance import Ambulance
from core.models.ambulance_service import AmbulanceService


def add_ambulance(request,pk):
    if request.method == "POST":
        new_ambulance_form = NewAmbulanceForm(request.POST)
        if new_ambulance_form.is_valid():
            registration_number = new_ambulance_form.cleaned_data['registration_number']
            dominant_color = new_ambulance_form .cleaned_data['dominant_color']
            car_model = new_ambulance_form .cleaned_data['car_model']
            make_year = new_ambulance_form .cleaned_data['make_year']

            ambulance_service = AmbulanceService.objects.get(id=1)
            ambulance = Ambulance(registration_number=registration_number,dominant_color=dominant_color,
                                  car_model=car_model,make_year=make_year,ambulance_service=ambulance_service,
                                  is_for_ambulance_service=True)

            messages.success(request, "Ambulance  Added Successfully")

        else:
            context = {'new_ambulance_form ': new_ambulance_form }
            return render(request, 'add_ambulance_service.html', context)

    new_ambulance_form = NewAmbulanceForm()

    context = {'new_ambulance_form': new_ambulance_form }
    return render(request, 'add_ambulance.html', context)

