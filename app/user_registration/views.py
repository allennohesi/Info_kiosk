import uuid
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from app.models import AuthUser, AuthUserGroups, AuthGroup
from django.db import transaction
from django.contrib.auth.hashers import make_password


def list_users(request):
    if request.method == "POST":
        check_username = AuthUser.objects.filter(username=request.POST.get('username'))
        check_email = AuthUser.objects.filter(email=request.POST.get('email'))
        if check_email:
            return JsonResponse({'error': True, 'msg': "Email '{}' is already existed.".format(request.POST.get('email'))})
        else:
            if not check_username:
                with transaction.atomic():
                    user = AuthUser(
                        first_name=request.POST.get('first_name'),
                        middle_name=request.POST.get('middle_name'),
                        last_name=request.POST.get('last_name'),
                        email=request.POST.get('email'),
                        username=request.POST.get('username'),
                        password=make_password(request.POST.get('password')),
                        is_superuser=True if request.POST.get('is_superuser') else False,
                        is_staff=True if request.POST.get('is_staff') else False,
                        is_active=1,
                        updated_by_id=request.user.id
                    )
                    user.save()

                    AuthUserGroups.objects.create(
                        user_id=user.id,
                        group_id=request.POST.get('group'),
                    )
                    return JsonResponse({'data': 'success', 'msg': "New user '{}' has been added successfully.".format(request.POST.get('username'))})
                return JsonResponse({'error': True, 'msg': 'Internal Error. An uncaught exception was raised.'})
            return JsonResponse({'error': True, 'msg': "User '{}' is already existed.".format(request.POST.get('username'))})



    context = {
        'at_group': AuthGroup.objects.all(),
    }
    return render(request, 'users/list_users.html', context)


def edit(request,pk):
    if request.method == "POST":
        AuthUser.objects.filter(id=pk).update(
            first_name=request.POST.get('first_name'),
            middle_name=request.POST.get('middle_name'),
            last_name=request.POST.get('last_name'),
        )
        full_name = request.POST.get('first_name') + " " +  request.POST.get('middle_name') + " " + request.POST.get('last_name')
        print(full_name)
        return JsonResponse({'data': 'success', 'msg': "Your new Name '{}' has been updated.".format(full_name)})
    context = {
        'user': AuthUser.objects.filter(id=pk).first(),
        'at_group': AuthGroup.objects.all(),
        'user_group': AuthUserGroups.objects.filter(user_id=pk).first(),
    }
    return render(request, 'users/edit_users.html', context)