from django.contrib import messages
from django.shortcuts import render

from core.forms.ambulance_service_form import SetAmbulanceServicePrice
from core.models.ambulance_rate import AmbulanceRate


def set_ambulance_price(request,):
    all_ambulance_rate = AmbulanceRate.objects.all()
    if request.method == "POST":
        set_ambulanceservice_price = SetAmbulanceServicePrice(request.POST)

        if set_ambulanceservice_price.is_valid():
            city = set_ambulanceservice_price.cleaned_data['city']
            minumum_rate = set_ambulanceservice_price .cleaned_data['minumum_rate']
            minumum_distance = set_ambulanceservice_price.cleaned_data['minumum_distance']
            rate_per_minumum_distance = set_ambulanceservice_price.cleaned_data['rate_per_minumum_distance']
            distance_unit = set_ambulanceservice_price.cleaned_data['distance_unit']

            if AmbulanceRate.objects.filter(city=city):
                messages.success(request, "City rate already set")
            else:

                ambulance_rate = AmbulanceRate(city=city,minumum_rate=minumum_rate,
                                               minumum_distance=minumum_distance,
                                               rate_per_minumum_distance=rate_per_minumum_distance,
                                               distance_unit=distance_unit)

                ambulance_rate.save()

                messages.success(request, "Ambulance Rate Added Successfully")

        else:
            context = {'set_ambulanceservice_price': set_ambulanceservice_price,
                       'all_ambulance_rate':all_ambulance_rate}
            return render(request, 'add_ambulance_service.html', context)

    set_ambulanceservice_price = SetAmbulanceServicePrice()

    context = {'set_ambulanceservice_price': set_ambulanceservice_price,
               "all_ambulance_rate":all_ambulance_rate}
    return render(request, 'set_vehicle_price.html', context)