from core.models.ambulance_service import AmbulanceService
from core.models.auth_user_demographic import AuthUserDemographic
from core.models.base_model import BaseModel, get_object_or_none
from django.db import models


class FCM_Token(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=255, null=True)

    @classmethod
    def get_user_token(cls,auth_user):
        return get_object_or_none(cls,user=auth_user).token

    @classmethod
    def set_user_token(cls,auth_user,token):
        # import pdb
        # pdb.set_trace()
        user_token = get_object_or_none(cls,user = auth_user)
        if user_token:
            if user_token.token == token:
                return True
            else:
                user_token.token = token
                user_token.save()
        else:
            user_token = cls(user=auth_user,token=token)
            user_token.save()
        return True





