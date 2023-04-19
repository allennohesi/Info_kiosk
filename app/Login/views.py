from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from app.models import AuthUser

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'), request=request)
        if user is not None and user.is_active:
            auth_login(request, user)
            return JsonResponse({'data': 'success'})
        else:
            return JsonResponse({'msg': 'Invalid username and password.'})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    user = AuthUser.objects.filter(id=request.user.id).first()
    context = {
        'title': 'Home'
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    try:
        auth_logout(request)
        del request.session['uid']
    except KeyError:
        pass
    return redirect(login)
