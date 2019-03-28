from django.conf.urls import url

from core.views import core_views, user_views, ambulance_views, home_views

__author__ = 'andrews'

app_name = "core"
urlpatterns = [
    url(r'^accounts/signin', home_views.signin, name="signin"),
    url(r'^accounts/signout', home_views.sign_out, name="signout"),

    url('dashboard', core_views.dashboard, name="dashboard"),
    url('ambulance-service/add', user_views.add_new_ambulance_service, name="add-ambulance-service"),
    url('ambulance-service/view', user_views.view_ambulance_services, name="view-ambulance-service"),
    url('ambulance-service-admin/(?P<pk>\d+)/add', user_views.add_ambulance_service_admin, name="add-ambulance-service-admin"),
    url('ambulance-service-driver/(?P<pk>\d+)/add', user_views.add_ambulance_driver, name="add-ambulance-driver"),
    url('ambulance/(?P<pk>\d+)/add', ambulance_views.add_ambulance, name="add-ambulance"),

]