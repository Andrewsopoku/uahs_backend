

from django.contrib.auth.decorators import user_passes_test


def user_in_groups(group_names):
    def is_in_group(user):
        return _is_user_belong_to_group(user, group_names)
    return user_passes_test(is_in_group, "/status/401")


def _is_user_belong_to_group(user, group_names):
    return bool(user.groups.filter(name__in=group_names))


def is_a_tax_officer():
    return user_in_groups(["Tax Officer"])