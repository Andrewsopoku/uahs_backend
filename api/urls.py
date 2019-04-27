from django.conf.urls import url

from api.views import user_views

__author__ = 'andrews'

app_name = "api"
urlpatterns = [
    url(r'^accounts/signin',user_views.signin , name="app-signin"),
    url(r'^accounts/register',user_views.patient_register , name="patient-register")

    ]
