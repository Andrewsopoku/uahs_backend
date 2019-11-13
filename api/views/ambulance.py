import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from core.models.ambulance import Ambulance
from core.models.ambulance_location import AmbulanceLocation
from core.models.ambulance_rate import AmbulanceRate


@csrf_exempt
def get_ambulance_initial_price(request):
    if request.method == "POST":
        try:
            city = request.POST['city']
            distance = request.POST['distance']

            cityrate = AmbulanceRate.objects.filter(city=city)
            if cityrate:
                response = json.dumps({'status': 'ok', 'standard_price':str(get_price(cityrate[0],distance,"standard")),
                                       'deluxe_price': str(get_price(cityrate[0], distance,"deluxe"))})


        except Exception as ex:
            response = json.dumps({'status': 'error', 'message':str(ex)})

    else:
        response = json.dumps({'status': 'error', 'message': "Method not allowed"})
    return HttpResponse(response, content_type='application/json')


def get_price(cityrate, distance, type="standard"):

    if eval(distance) <= eval(cityrate.minumum_distance):
        price = eval(cityrate.minumum_rate)

    else:
        price = eval(distance) * eval(cityrate.rate_per_minumum_distance)

    if type == "deluxe":
        price = price * eval(cityrate.deluxe_rate)
    return round(price,2)

@csrf_exempt
def get_num_ambulance_available(request):
    if request.method == "POST":
        try:
            user_latitude= request.POST['from_latitude']
            user_longitude = request.POST['from_longitude']
            city

            cityrate = AmbulanceRate.objects.filter(city=city)
            if cityrate:
                response = json.dumps({'status': 'ok', 'price':str(get_price(cityrate[0],distance))})


        except Exception as ex:
            response = json.dumps({'status': 'error', 'message':str(ex)})

    else:
        response = json.dumps({'status': 'error', 'message': "Method not allowed"})
    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def set_ambulance_last_location(request):
    ambulance_latitude = request.POST['current_latitude']
    ambulance_longitude = request.POST['current_longitude']
    reg_num = request.POST['ambulance_reg_num']
    ambulance = Ambulance.get_ambulance_with_reg_num(reg_num)
    if AmbulanceLocation.create_or_edit(ambulance=ambulance,long=ambulance_longitude,
                                     lat=ambulance_latitude):
        response = json.dumps({'status': 'ok', 'message':"Location added"})
    else:
        response = json.dumps({'status': 'error', 'message': "Location not added"})
    return HttpResponse(response, content_type='application/json')
