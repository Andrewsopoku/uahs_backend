

from django.conf import settings

from core.custom_decorator import _is_user_belong_to_group
from core.models.ambulance_service_admin import AmbulanceServiceAdmin
from core.models.auth_user_demographic import AuthUserDemographic
from core.models.health_service_admin import HealthServiceAdmin


class CoreMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:

            if request.user.groups.filter(name='Ambulance Admin').exists() :
                reg = AuthUserDemographic.objects.get(user=request.user)
                company = AmbulanceServiceAdmin.objects.get(user=reg)
                request.reg = reg
                request.company = company
            elif request.user.groups.filter(name='Health Service Admin').exists() :
                reg = AuthUserDemographic.objects.get(user=request.user)
                company = HealthServiceAdmin.objects.get(user=reg)
                request.reg = reg
                request.company = company
                company.health_service.get_ambulance_service()



        response = self.get_response(request)

        return response
