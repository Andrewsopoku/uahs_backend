from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

def get_object_or_none(model, **kwargs):
    try:
        result = model.objects.get(**kwargs)
    except model.DoesNotExist:
        result = None
    return result