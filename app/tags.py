from django import template
from app.models import AuthUser, AuthUserGroups

register = template.Library()

@register.filter
def check_group_permission(user, group_name):
    if user.groups.filter(name=group_name).exists():
        return True
    return False

@register.simple_tag
def get_user_info(user_id):
    return AuthUser.objects.filter(id=user_id).first().get_fullname

@register.simple_tag
def get_user_role(user_id):
    return AuthUserGroups.objects.filter(user_id=user_id).first().group.name

