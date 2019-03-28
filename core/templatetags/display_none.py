from django.template import Library

register = Library()


@register.filter(name='display_none')
def display_none(value):
    if value is None:
        return "None"
    if len(value.strip()) == 0:
        return "None"

    return value