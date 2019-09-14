import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from api.views.ambulance import get_price
from core.core_util import send_driver_request_notification, send_patient_accept_notification, get_area, calc_dist, \
    send_patient_tripstart_notification, send_party_tripend_notification
from core.models.ambulance import Ambulance
from core.models.ambulance_driver_assignment import AmbulanceDriverAssignment
from core.models.ambulance_location import AmbulanceLocation
from core.models.ambulance_rate import AmbulanceRate
from core.models.app_fcm_token import FCM_Token
from core.models.auth_user_demographic import AuthUserDemographic
from core.models.base_model import get_object_or_none
from core.models.transaction import Transaction

START_TRIP = "Patient Picked Up"
END_TRIP ="Trip Ended"
WAIT_FOR_DRIVER = "Waiting For Driver"
DRIVER_ACCEPT_REQUEST = "Request Accepted"
TRIP_TRUNCATED = "Trip Truncated"


@csrf_exempt
def find_driver(request):
    if request.method == "POST":
        try:
            init_from_lat = request.POST['from_lat']
            init_to_lat = request.POST['to_lat']
            init_from_long = request.POST['from_long']
            init_to_long = request.POST['to_long']
            user_id = request.POST['user_id']
            patient = AuthUserDemographic.get_user_by_id(user_id)

            distance = request.POST['distance']
            import pdb
            #pdb.set_trace()

            trans = Transaction(init_from_lat=init_from_lat,init_to_lat=init_to_lat,
                                init_from_long=init_from_long,init_to_long=init_to_long,
                                init_distance=distance,status="Waiting For Driver",
                                patient=patient)
            trans.save()

            closest_ambulance = AmbulanceLocation.get_closest_ambulance(lat_a=init_from_lat,long_a=init_from_long)
            driver = AmbulanceDriverAssignment.get_ambulance_driver(closest_ambulance.ambulance).driver

            send_driver_request_notification(driver.user,trans)

            response = json.dumps({'status': 'ok', 'message': "Connecting to Ambulance","transaction_id":trans.id})
        except Exception as ex:
            response = json.dumps({'status': 'error', 'message': str(ex)})

    else:
        response = json.dumps({'status': 'error', 'message': "Method not allowed"})
    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def accept_ambulance_request(request):
    if request.method == "POST":
        try:
            transaction_id = request.POST['transaction_id']
            user_id = request.POST['user_id']
            registration_number = request.POST['registration_number']
            ambulance = Ambulance.get_ambulance_with_reg_num(registration_number)
            driver = AuthUserDemographic.get_user_by_id(user_id)


            import pdb
            #pdb.set_trace()

            trans = get_object_or_none(Transaction,id = transaction_id)
            if trans:
                trans.driver = driver
                trans.ambulance = ambulance
                trans.status = "Request Accepted"
                trans.save()

                send_patient_accept_notification(trans.patient,trans)

            response = json.dumps({'status': 'ok', 'message': "Go to Patient Location",
                                   "patient_lat":trans.init_from_lat,'patient_long':trans.init_from_long,
                                   'patient_name':trans.patient.first_name,'patient_mobile':trans.patient.mobile})
        except Exception as ex:
            response = json.dumps({'status': 'error', 'message': str(ex)})

    else:
        response = json.dumps({'status': 'error', 'message': "Method not allowed"})
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def start_trip(request):
    if request.method == "POST":
        try:
            final_from_lat = request.POST['final_from_lat']
            final_from_long = request.POST['final_from_long']
            trans_id = request.POST['transaction_id']
            user_id = request.POST['user_id']
            driver = AuthUserDemographic.get_user_by_id(user_id)


            import pdb
            #pdb.set_trace()

            trans = Transaction.objects.get(id = trans_id)
            trans.final_from_lat = final_from_lat
            trans.final_from_long = final_from_long
            trans.status = "Patient Picked Up"
            trans.save()

            send_patient_tripstart_notification(trans.patient,trans)

            response = json.dumps({'status': 'ok', 'init_to_lat':trans.init_to_lat,
                                   'init_to_long':trans.init_to_long,
                                   'area':get_area(trans.init_to_lat,trans.init_to_long)})

        except Exception as ex:
            response = json.dumps({'status': 'error', 'message': str(ex)})

    else:
        response = json.dumps({'status': 'error', 'message': "Method not allowed"})
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def end_trip(request):
    if request.method == "POST":
        try:
            final_to_lat = request.POST['final_to_lat']
            final_to_long = request.POST['final_to_long']
            trans_id = request.POST['transaction_id']
            user_id = request.POST['user_id']
            user = AuthUserDemographic.get_user_by_id(user_id)


            import pdb
            #pdb.set_trace()

            trans = Transaction.objects.get(id = trans_id)



            trans.final_to_lat = final_to_lat
            trans.final_to_long = final_to_long

            trans.save()

            if trans.status == START_TRIP:
                trans.status = END_TRIP
                distance = calc_dist(eval(str(trans.final_from_lat)), eval(str(trans.final_from_long)),
                                               eval(str(trans.final_to_lat)), eval(str(trans.final_to_long)))
                trans.final_distance = distance
                cityrate = AmbulanceRate.objects.filter(city="Accra")
                price = get_price(cityrate[0], str(distance))
                trans.final_charge = str(price)
                response = json.dumps({'status': 'ok','truncated': False, 'charge': str(price)})
            else:
                trans.status = TRIP_TRUNCATED
                response = json.dumps({'status': 'ok', 'truncated': True})
            trans.save()

            if user.is_ambulance_driver():
                send_party_tripend_notification(trans.patient,trans)
            else:
                send_party_tripend_notification(trans.driver, trans)

        except Exception as ex:
            response = json.dumps({'status': 'error', 'message': str(ex)})

    else:
        response = json.dumps({'status': 'error', 'message': "Method not allowed"})
    return HttpResponse(response, content_type='application/json')
