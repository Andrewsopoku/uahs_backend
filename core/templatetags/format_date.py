from django.template import Library

register = Library()


@register.filter(name='format_date')
def format_date(current_date):
    if current_date:
        return current_date.strftime("%B %d, %Y %r")
    return ''

@register.filter(name='date_only_format')
def date_only_format(current_date):
    if current_date:
        return current_date.strftime("%B %d, %Y")
    return ''

@register.filter(name='format_set_by')
def format_set_by(code, user):
    set_by = '%s at %s' % (code.updated_by, format_date(code.updated_at))
    if (code.is_used() or code.is_breached()) and not user.get_profile().is_mpedigree_admin():
        import re

        return re.sub(r"Checked by \d+", "Checked by patient", set_by)
    return set_by
