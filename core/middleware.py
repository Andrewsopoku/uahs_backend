

from django.conf import settings

from core.custom_decorator import _is_user_belong_to_group
from core.models.ambulance_service_admin import AmbulanceServiceAdmin
from core.models.auth_user_demographic import AuthUserDemographic


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

                print(reg)
                print(company)

        response = self.get_response(request)

        return response
