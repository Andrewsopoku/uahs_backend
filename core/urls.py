from django.conf.urls import url

from core.views import core_views, user_views, ambulance_views, home_views,\
    driver_view, health_service_view
from core.views.settings_views import set_ambulance_price

__author__ = 'andrews'

app_name = "core"
urlpatterns = [
    url(r'^accounts/signin', home_views.signin, name="signin"),
    url(r'^accounts/signout', home_views.sign_out, name="signout"),

    url('dashboard', core_views.dashboard, name="dashboard"),
    url('ambulance-service/(?P<pk>\d+)/detail', core_views.ambulance_service_detail, name="ambulance-service-detail"),

    url('ambulance-service/add', user_views.add_new_ambulance_service, name="add-ambulance-service"),
    url('ambulance-service/view', user_views.view_ambulance_services, name="view-ambulance-service"),

    url('ambulance-service-admin/(?P<pk>\d+)/add', user_views.add_ambulance_service_admin, name="add-ambulance-service-admin"),
    url('ambulance-service-driver/(?P<pk>\d+)/add', user_views.add_ambulance_driver, name="add-ambulance-driver"),
    url('ambulance-service-driver/(?P<pk>\d+)/view', driver_view.list_driver, name="view-ambulance-driver"),
    url('ambulance-service-driver/(?P<driver_pk>\d+)/(?P<new_status>[-\w]+)/change', driver_view.change_driver_status, name="change-driver-status"),

    url('ambulance/(?P<pk>\d+)/add', ambulance_views.add_ambulance, name="add-ambulance"),
    url('ambulance/(?P<ambulance_pk>\d+)/(?P<new_status>[-\w]+)/change', ambulance_views.change_ambulance_status, name="change-ambulance-status"),
    url('ambulance/(?P<pk>\d+)/list', ambulance_views.list_ambulance, name="ambulance-list"),
    url('ambulance-service/(?P<pk>\d+)/add', ambulance_views.add_ambulance, name="add-ambulance"),
    url('ambulance-service/(?P<pk>\d+)/driver/assign', driver_view.assign_driver_to_ambulance, name="assign-driver-ambulance"),

    url('health-service/add', health_service_view.add_new_health_service, name="add-health-service"),
    url('health-service/view', health_service_view.view_health_services, name="view-health-service"),
    url('health-service-admin/(?P<pk>\d+)/add', user_views.add_health_service_admin,
        name="add-health-service-admin"),
    url('health-service/(?P<pk>\d+)/add-ambulance-service', health_service_view.add_ambulance_service_to_health_service,
        name="add-ambulance-service-to-health-service"),



    url('setting/set-ambulance-price', set_ambulance_price,
        name="set-ambulance-price")
]