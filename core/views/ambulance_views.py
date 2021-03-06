from django.contrib import messages
from django.shortcuts import render, redirect

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
            type = new_ambulance_form.cleaned_data['type']

            ambulance_service = AmbulanceService.objects.get(id=pk)
            ambulance = Ambulance(registration_number=registration_number,dominant_color=dominant_color,
                                  car_model=car_model,make_year=make_year,ambulance_service=ambulance_service,
                                  is_for_ambulance_service=True, type=type)
            ambulance.save()

            messages.success(request, "Ambulance  Added Successfully")

        else:
            context = {'new_ambulance_form ': new_ambulance_form }
            return render(request, 'add_ambulance_service.html', context)

    new_ambulance_form = NewAmbulanceForm()

    context = {'new_ambulance_form': new_ambulance_form }
    return render(request, 'add_ambulance.html', context)

def list_ambulance(request,pk):
    ambulance_service = AmbulanceService.objects.get(id=pk)
    ambulance_list = Ambulance.objects.filter(ambulance_service=ambulance_service)
    context = {"ambulance_list":ambulance_list}
    return render(request, 'ambulance_list.html',context)

def change_ambulance_status(request,ambulance_pk,new_status):
    ambulance = Ambulance.objects.get(id = ambulance_pk)
    if ambulance:
        ambulance.status = new_status
        ambulance.save()

    return redirect(request.META['HTTP_REFERER'])
