import random
import string

from django.http import HttpResponse
from django.template.loader import get_template
from pyfcm import FCMNotification

from core.mailer import Mailer
from core.models.app_fcm_token import FCM_Token

__author__ = 'andrews'

sender = "account@uahsghana.com"

def add_zeros(length,code):
    while(len(code)<length):
          code = "0"+code
    return  code

def randomPassword():
    """Generate a random password """
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    for i in range(6):
        password += random.choice(randomSource)
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    password = password.replace(" ","")
    return password


driver_app_server_key = 'AAAAGZUKcXQ:APA91bF3UhsJlJAUrvi3LLinQoFbvdD8PYEgTz1wx1yHgy4ssLMEG_JWZo6r5TgueW-4ayDeuOmygmZAERChgDlIfrTM9oewYePC6rElVHIRHEUtu057JrgvSAtxxqVLp6S51ZWMXdu3'
patient_app_server_key = 'AAAAtXViVgs:APA91bGTfuritNLiIeXzqKqIQFeNWpbcgQYQRm6Wot2CPsKBAUgISEAhG0vSo0b5XhqbSHopmd2kfFTuynzuAQnPnvH4ryBo2jVlUTEw0Op78vgKUNilPAKkUJ1njUbBpIB5_-qqGBxJ'

def send_driver_request_notification(user,trans):

    data={'transaction_id':trans.id,
          "area": get_area(trans.init_from_lat,trans.init_from_long),
          'title':'Request Notification'}
    path_to_fcm = "https://fcm.googleapis.com"
    reg_id = FCM_Token.get_user_token(user)  # quick and dirty way to get that ONE fcmId from table
    message_title = "Ambulance Request"
    message_body = "Request from {}!".format(get_area(trans.init_from_lat,trans.init_from_long))
    result = FCMNotification(api_key=driver_app_server_key).notify_single_device(registration_id=reg_id,
                                                                      message_title=message_title,
                                                                      message_body=message_body,
                                                                      data_message=data,
                                                                                 sound="beyond_doubt_2.mp3")
    return HttpResponse(result)

def send_patient_accept_notification(user,trans):
    from core.models.ambulance_location import AmbulanceLocation
    data = {'transaction_id': trans.id,
            "ambulance_color": trans.ambulance.dominant_color,
            "title": "Ambulance Accept Request",
            "patient_lat": trans.init_from_lat,
            "patient_long": trans.init_from_long,
            "driver_lat": AmbulanceLocation.objects.get(ambulance=trans.ambulance).lat,
            "driver_long": AmbulanceLocation.objects.get(ambulance=trans.ambulance).long,
            "driver_name":trans.driver.first_name,
            "driver_mobile":trans.driver.mobile,
            "ambulance_number":trans.ambulance.registration_number,

            }

    path_to_fcm = "https://fcm.googleapis.com"
    reg_id = FCM_Token.get_user_token(user)  # quick and dirty way to get that ONE fcmId from table
    message_title = "Ambulance Coming"
    message_body = "Ambulance {} is coming!".format(trans.ambulance.registration_number,)
    result = FCMNotification(api_key=patient_app_server_key).notify_single_device(registration_id=reg_id,
                                                                      message_title=message_title,
                                                                      message_body=message_body,
                                                                      data_message=data,
                                                                                  sound="beyond_doubt_2.mp3")
    print(result)
    return HttpResponse(result)

def send_patient_tripstart_notification(user,trans):
    data={'transaction_id':trans.id,
          "title": "Trip Started",
          "patient_to_lat": trans.init_to_lat,
          "patient_to_long": trans.init_to_long,
          "patient_from_lat":trans.final_from_lat,
          "patient_from_long":trans.final_from_long
           }

    path_to_fcm = "https://fcm.googleapis.com"
    reg_id = FCM_Token.get_user_token(user)  # quick and dirty way to get that ONE fcmId from table
    message_title = "Trip started"
    message_body = "Trip to {} has started!".format(get_area(trans.init_to_lat,trans.init_to_long))
    result = FCMNotification(api_key=patient_app_server_key).notify_single_device(registration_id=reg_id,
                                                                      message_title=message_title,
                                                                      message_body=message_body,
                                                                      data_message=data,
                                                                                  sound="beyond_doubt_2.mp3")
    print(data,result)
    return HttpResponse(result)


def send_party_tripend_notification(user,trans):
    from api.views.transactions import END_TRIP
    truncated = True
    if trans.status == END_TRIP:
        truncated = False
    else:
        truncated = True
    data={'transaction_id':trans.id,
          "title": "Trip Ended",
          'charge':trans.final_charge,
          'truncated':truncated
           }
    api_key = patient_app_server_key
    if user.is_ambulance_driver():
        api_key = driver_app_server_key

    path_to_fcm = "https://fcm.googleapis.com"
    reg_id = FCM_Token.get_user_token(user)  # quick and dirty way to get that ONE fcmId from table
    message_title = "Trip Ended"
    message_body = "Trip to {} has ended!".format(get_area(trans.init_to_lat,trans.init_to_long))
    result = FCMNotification(api_key=api_key).notify_single_device(registration_id=reg_id,
                                                                      message_title=message_title,
                                                                      message_body=message_body,
                                                                      data_message=data,
                                                                      sound="beyond_doubt_2.mp3")


    print(result)
    return HttpResponse(result)

from math import sin, cos, radians, degrees, acos

def calc_dist(lat_a, long_a, lat_b, long_b):
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    long_diff = radians(long_a - long_b)
    distance = (sin(lat_a) * sin(lat_b) +
                cos(lat_a) * cos(lat_b) * cos(long_diff))
    return degrees(acos(distance)) * 69.09

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="UAHS_Backend",timeout=3)


def get_area(lat_a,long_a):
    if lat_a and long_a:
        location = geolocator.reverse("{}, {}".format(lat_a,long_a))
        area = location.address.split(',')
        return "{} {}, {}".format(area[0],area[1],area[2])
    else:
        return "Unknown Location"

url = "https://api.hubtel.com/v1/messages/send"
import requests

def send_pin_register(to_contact,pin):
    message = "Thanks for registering for UAHS services. Download UAHS app at .Your password is "+str(pin)
    querystring = {"From": "UAHS Mobile", "To": to_contact, "Content": message, "ClientID": "eferjnka",
                   "ClientSecret": "gcpgrhcn"}

    response = requests.request("GET", url, params=querystring)

    print(response.text)

def send_pin_register_patient(to_contact,pin):
    message = "Thanks for registering for UAHS services. Your pin is "+str(pin)
    querystring = {"From": "UAHS Mobile", "To": to_contact, "Content": message, "ClientID": "eferjnka",
                   "ClientSecret": "gcpgrhcn"}

    response = requests.request("GET", url, params=querystring)

    print(response.text)


def _sending_enterprise_acc_creation_password(auth_user, password):
    #registration = get_object_or_none(CompanyRegistration, pk=registration_id)
        htmly = get_template('emails/enterprise_account_creation_email.html')
        d = {'firstname': auth_user.first_name, 'password': password,}
        message = htmly.render(d)


        Mail = Mailer()
        Mail.send_message(to=auth_user.email, sender=sender, subject="UMobile Registration", message=message)


def _sending__acc_reset_password(auth_user, password):
    #registration = get_object_or_none(CompanyRegistration, pk=registration_id)
        htmly = get_template('emails/account_reset_email.html')
        d = {'firstname': auth_user.first_name, 'password': password,}
        message = htmly.render(d)


        Mail = Mailer()
        Mail.send_message(to=auth_user.email, sender=sender, subject="UMobile Account", message=message)


