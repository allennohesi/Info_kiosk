from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from app.createPost.models import createdPost, uploadfile, upload_profile, location_picture, createFeedback
from django.views.decorators.csrf import csrf_exempt
import requests
from django.core.paginator import Paginator
import json
from datetime import datetime
import os
currentMonth = datetime.now().month
today = datetime.now()

def landingpage(request):
    # vacancy = requests.get('https://caraga-iris-internal.dswd.gov.ph/api/vacancies/process/', headers={'Content-Type': 'application/json',
    #                                     'Authorization': 'Token {}'.format('243f229926212da6b5170d5e604a038d28fec9f4')})
    
    # # print(vacancy.json())
    
    # current = today.strftime('%B %d, %Y')


    context = {
          'feedback': createFeedback.objects.all().order_by('-id'),
        #   'value': vacancy.json(),
        #   'current': current,
    }
    return render(request,'landingpage.html', context)

@csrf_exempt
def deletefeedback(request):
	if request.method == "POST":
		createFeedback.objects.filter(id=request.POST.get('id')).delete()
	return JsonResponse({'data': 'success'})


def proceed(request):
    return render(request,'InternalExternal.html')


def FrontlineServices(request): #NON FRONTLINE SERVICES
    data = createdPost.objects.filter(services_type="Frontline Services")

    context = {
        'data':data,
    }
    return render(request, 'FrontlineServices.html', context)

def NonFrontlineServices(request): #FRONTLINE SERVICES
    data = createdPost.objects.filter(services_type="Non-Frontline Services")
    context = {
        'data':data,
    }
    return render(request, 'NonFrontlineServices.html', context)

def indexData(request,pk):
    picture = upload_profile.objects.filter(created_id=pk).first()
    created_post = createdPost.objects.filter(id=pk).first()

    uploaded_specific = uploadfile.objects.filter(title_id=pk).first() #TO GET THE FIRST UPLOADED AND MATCH TO ALL UPLOADED
    
    uploaded = uploadfile.objects.filter(title_id=pk,file_ext=".pdf").order_by('id')
    uploaded_video = uploadfile.objects.filter(title_id=pk,file_ext=".mp4").order_by('id')

    context = {
        'profile': picture,
        'uploaded': uploaded,
        'created_post': created_post,
        'uploaded_specific': uploaded_specific,
        'uploaded_video': uploaded_video
    }
    return render(request, 'detailsPost.html', context)

def modalforData(request,pk):
    context = {
        'location_data': location_picture.objects.filter(created_id=pk).first(),
        'created_post':createdPost.objects.filter(id=pk).first(),
    }
    return render(request, 'layout/modalForMap.html', context)

def uploadFeedback(request):
	if request.method == "POST":
		feedback = createFeedback.objects.create(
			subject=request.POST.get('subject'),
			message=request.POST.get('message'),
            mood=request.POST.get('mood'),
            sex=request.POST.get('sex'),
		)
		return JsonResponse({'msg': 'You successfully submitted your feedback'})

def modalforpdfviewing(request,pk):
      print("THIS IS TEST",pk)
      data = uploadfile.objects.filter(id=pk).first()
      context = {
            'dataFiles': data
      }
      return render(request, 'pdfviewingmodal.html', context)

def vacancies(request):
    vacancy = requests.get('https://caraga-iris-internal.dswd.gov.ph/api/vacancies/process/', headers={'Content-Type': 'application/json',
                                        'Authorization': 'Token {}'.format('243f229926212da6b5170d5e604a038d28fec9f4')})

    current = today.strftime('%B %d, %Y')

    context = {
          'value': vacancy.json(),
          'current': current,
    }
    return render(request, 'vacancies.html', context)