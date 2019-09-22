import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.views.ambulance import get_price
from api.views.transactions import END_TRIP
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

@csrf_exempt
def get_trips(request):
    response = {}
    user_id = request.POST['user_id']
    response["transactions"] = []
    user = AuthUserDemographic.get_user_by_id(user_id=user_id)
    if user.is_ambulance_driver():
        trips = Transaction.objects.filter(driver=user,status=END_TRIP )
    else:
        trips = Transaction.objects.filter(patient=user)

    for transaction in list(trips):
        temp = {}
        temp["id"] = transaction.id
        temp["from_lat"] = transaction.final_from_lat
        temp["from_long"] = transaction.final_from_long
        temp["to_lat"] = transaction.final_to_lat
        temp["to_long"] = transaction.final_to_long
        temp["date"] = str(transaction.created_at.date())

        temp["from_area"] = get_area(transaction.final_from_lat,transaction.final_from_long)
        temp["to_area"] = get_area(transaction.final_to_lat,transaction.final_to_long)
        temp["charge"] = transaction.final_charge
        temp["status"] = transaction.status

        response["transactions"].append(temp)
    response["status"] = "ok"
    print(response)
    return JsonResponse(response, content_type='application/json')
