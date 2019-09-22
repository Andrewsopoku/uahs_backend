from django.conf.urls import url

from api.views import user_views, ambulance, ambulance_driver, transactions, trip_views

__author__ = 'andrews'

app_name = "api"
urlpatterns = [
    url(r'^accounts/signin',user_views.signin , name="app-signin"),
    url(r'^accounts/reset_password',user_views.reset_password , name="app-resetpassword"),
    url(r'^accounts/register',user_views.patient_register , name="patient-register"),
    url(r'^ambulance/get-initial-price',ambulance.get_ambulance_initial_price , ),
    url(r'^driver/get-information',ambulance_driver.get_information , ),
    url(r'^driver/change_status',ambulance_driver.change_status , ),
    url(r'^ambulance/add-last-location',ambulance.set_ambulance_last_location , ),
    url(r'^account/add-token',user_views.add_token, ),
    url(r'^ambulance/find_ambulance',transactions.find_driver, ),
    url(r'^ambulance/accept_request',transactions.accept_ambulance_request, ),
    url(r'^ambulance/start_trip',transactions.start_trip, ),
    url(r'^ambulance/end_trip',transactions.end_trip, ),
    url(r'^user/get_trip',trip_views.get_trips, ),




    ]
