import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from core.models.ambulance_driver import AmbulanceDriver
from core.models.ambulance_driver_assignment import AmbulanceDriverAssignment
from core.models.auth_user_demographic import AuthUserDemographic


@csrf_exempt
def get_information(request):
    if request.method == "POST":
        try:
            user_id = request.POST['user_id']
            user = AuthUserDemographic.objects.get(id= user_id)
            ambulance_driver = AmbulanceDriver.objects.get(user=user)
            driver_assignment = AmbulanceDriverAssignment.objects.filter(driver=ambulance_driver,status="Active")
            if driver_assignment:
                driver_assignment = driver_assignment[0]
                response = json.dumps({'status': 'ok',
                                       'ambulance':driver_assignment.ambulance.registration_number,
                                       'driver_status':ambulance_driver.status})
            else:
                response = json.dumps({'status': 'ok',
                                       'message': "No Ambulance Assigned",
                                       'driver_status':ambulance_driver.status})



        except Exception as ex:
            response = json.dumps({'status': 'error', 'message':str(ex)})

    else:
        response = json.dumps({'status': 'error', 'message': "Method not allowed"})
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def change_status(request):
    if request.method == "POST":
        try:
            user_id = request.POST['user_id']
            new_status = request.POST['new_status']
            user = AuthUserDemographic.objects.get(id= user_id)
            ambulance_driver = AmbulanceDriver.objects.get(user=user)
            ambulance_driver.status = new_status
            ambulance_driver.save()
            response = json.dumps({'status': 'ok',
                                   'message': "status changed",})

        except Exception as ex:
            response = json.dumps({'status': 'error', 'message': str(ex)})

    else:
        response = json.dumps({'status': 'error', 'message': "Method not allowed"})
    return HttpResponse(response, content_type='application/json')
