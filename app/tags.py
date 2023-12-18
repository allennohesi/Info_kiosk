from django import template
from app.models import AuthUser, AuthUserGroups
from datetime import date, datetime, timedelta
import os
import requests
currentMonth = datetime.now().month
register = template.Library()
today = datetime.now()

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

@register.simple_tag
def check_if_deadline(deadline_at, date):
    date_today_formatted = datetime.strptime(date, '%B %d, %Y').date()
    deadline_at_formatted = datetime.strptime(deadline_at, '%B %d, %Y').date()
    if date_today_formatted <= deadline_at_formatted:
        return True
    else:
        return False

# @register.simple_tag
# def getallData():
    # vacancy = requests.get('https://caraga-iris-internal.dswd.gov.ph/api/vacancies/process/', headers={'Content-Type': 'application/json',
    #                                     'Authorization': 'Token {}'.format('243f229926212da6b5170d5e604a038d28fec9f4')})

    # current_month = today.strftime("%b")
    # data_value = row['deadline_at']
    # data_value.split(" ")[0]
    # if current_month == data_value.split(" ")[0]:
    #     values = row['position']+ " \n " + row['deadline_at'] 

    #     print("------------------------",values)
    #     return values
    