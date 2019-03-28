from django import template

register = template.Library()


@register.inclusion_tag('pagination.html')
def pagination(paginator):
    return {"paginator": paginator}
