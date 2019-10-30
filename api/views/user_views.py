import datetime
from random import random

from countries_plus.models import Country
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render

from core.core_util import add_zeros, send_driver_request_notification, send_pin_register_patient
from core.models.app_fcm_token import FCM_Token
from core.models.auth_user_demographic import AuthUserDemographic

# Create your views here.

import json

from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('email','')
        password = request.POST.get('password','')

        if username and password:

            user = authenticate(request, username=username, password=password)

            if user is not None:
                    user_serial = AuthUserDemographic.objects.get(user= user)

                    if user_serial.first_login:
                        pin = random.randint(1000, 9999)
                        send_pin_register_patient(user_serial.mobile,pin)
                        response = json.dumps({'status': 'ok',
                                               'user_id': user_serial.id,
                                               'first_time':user_serial.first_login,
                                               'name':'{} {}'.format(user_serial.first_name,user_serial.surname),
                                               'p_id': user_serial.unique_id,
                                               'group':str(user_serial.get_user_group()),
                                               'pin':pin,
                                               })
                    else:
                        response = json.dumps({'status': 'ok',
                                               'user_id': user_serial.id,
                                               'first_time':user_serial.first_login,
                                               'name':'{} {}'.format(user_serial.first_name,user_serial.surname),
                                               'p_id': user_serial.unique_id,
                                               'group':str(user_serial.get_user_group()),
                                               })


            else:
                    response = json.dumps({'status': 'error', 'message': "Wrong email or password"})
        else:
            response = json.dumps({'status': 'error', 'message': "Email or password not provided"})

    else:
        response = json.dumps({'status': 'error', 'message': "something went wrong"})

    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id','')
        password = request.POST.get('newPassword','')

        if user_id and password:
            demoUser = AuthUserDemographic.objects.get(id=user_id)
            user = demoUser.user
            user.set_password(password)
            user.save()
            demoUser.first_login = False
            demoUser.save()

            response = json.dumps({'status': 'ok', })

        else:
                    response = json.dumps({'status': 'error', 'result': "Invalid data"})

    else:
        response = json.dumps({'status': 'error', 'result': "something went wrong"})

    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def activate_by_pin(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id','')

        if user_id :
            demoUser = AuthUserDemographic.objects.get(id=user_id)
            demoUser.first_login = False
            demoUser.save()

            response = json.dumps({'status': 'ok', })

        else:
            response = json.dumps({'status': 'error', 'message': "Invalid data"})

    else:
        response = json.dumps({'status': 'error', 'message': "something went wrong"})

    return HttpResponse(response, content_type='application/json')




@csrf_exempt
def patient_register(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            countrycode = request.POST['country_code']
            phone_number = request.POST['phone_number']

            try:
                user = User.objects.create_user(username=email, password=password,)
                user.groups.add(Group.objects.get_or_create(name="Patient")[0])
                user.save()
            except Exception as ab:
                response = json.dumps({'status': 'error', 'message': 'Account already exist'})


            else:
                now = datetime.datetime.now()
                user_info = AuthUserDemographic(user=user, email=email,
                                                    nationality=Country.objects.get(iso=countrycode).name,
                                                    mobile=phone_number)
                user_info.save()
                user_info.unique_id = 'PA{}{}{}{}'.format(now.day, now.month,
                                                            now.year, add_zeros(5, str(user_info.id)))

                user_info.save()


                response = json.dumps({'status': 'ok','message':'Account has been created successfully'})

        except Exception as exs:
            message = exs.args
            response = json.dumps({'status': 'error', 'message': message})

    else:
        response = json.dumps({'status': 'error', 'message': "something went wrong"})

    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def profile(request):
    try:
        if request.method == 'POST':

            username = request.POST.get('user_id','')
            password = request.POST.get('password','')

            if username and password:

                user = authenticate(request, username=username, password=password)

                if user is not None:
                        user_serial = AuthUserDemographic.objects.get(user= user)



                        response = json.dumps({'status': 'ok', 'user_id': user_serial.id,
                                               'first_time':user_serial.first_login, "name":"{} {}".format(user_serial.first_name,
                                                                                                           user_serial.surname),
                                               'p_id':user_serial.unique_id})

                else:
                        response = json.dumps({'status': 'error', 'message': "Wrong username or password"})
            else:
                response = json.dumps({'status': 'error', 'message': "Username or password not provided"})

    except:
            response = json.dumps({'status': 'error', 'message': "something went wrong"})

    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def add_token(request):
    try:
        if request.method == 'POST':

            user_id = request.POST.get('user_id','')
            token = request.POST.get('token','')
            # import pdb
            # pdb.set_trace()

            if user_id and token:
                    user_serial = AuthUserDemographic.objects.get(id=user_id)
                    FCM_Token.set_user_token(auth_user=user_serial,token=token)
                    #send_driver_request_notification(user_serial)

                    response = json.dumps({'status': 'ok', 'message':"Token saved"})

            else:
                response = json.dumps({'status': 'error', 'message': "Wrong username or password"})

    except:
            response = json.dumps({'status': 'error', 'message': "something went wrong"})

    return HttpResponse(response, content_type='application/json')

