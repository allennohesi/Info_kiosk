from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from app.createPost.models import createdPost, uploadfile, upload_profile, location_picture, createFeedback, iecMaterial, number_db
from django.views.decorators.csrf import csrf_exempt
import requests
from django.core.paginator import Paginator
import json
from datetime import datetime
import os
from rest_framework.authtoken.models import Token

currentMonth = datetime.now().month
today = datetime.now()


current = today.strftime('%B %d, %Y')

def landingpage(request):        

	services = createdPost.objects.filter(type="FT").order_by('-id')
	
	context = {
		'feedback': createFeedback.objects.all().order_by('-id'),
		'services': services,
	}
	return render(request,'landingpage.html', context)

def slideshow(request):
	 return render(request,'slideshow.html')

def printQue(request): #NON FRONTLINE SERVICES
	queNumber = number_db.objects.all().using('queing').last(),
	context = {
		'data':queNumber,
		'dateToday': current,
	}
	return render(request, 'printQUE.html', context)

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
	uploaded_specific = uploadfile.objects.filter(title_id=pk, language_status=0).first() #TO GET THE FIRST UPLOADED AND MATCH TO ALL UPLOADED
	uploaded = uploadfile.objects.filter(title_id=pk,file_ext=".pdf", language_status=0).order_by('id')[:8]
	local_dialect_specific = uploadfile.objects.filter(title_id=pk,language_status=1).first() #GetTheFirstUploadedDataLocalDialect
	local_dialect = uploadfile.objects.filter(title_id=pk,file_ext=".pdf",language_status=1).order_by('id')[:8]
	context = {
		'profile': picture,
		'created_post': created_post,

		'uploaded': uploaded,
		'uploaded_specific': uploaded_specific,

		'local_dialect_specific': local_dialect_specific,
		'local_dialect': local_dialect,
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
	data = uploadfile.objects.filter(id=pk).first()
	context = {
		'dataFiles': data
	}
	return render(request, 'pdfviewingmodal.html', context)


def vacancies(request):
	current_date = today.strftime('%B %d, %Y')
	from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
	vacancy = requests.get('https://caraga-iris.dswd.gov.ph/api/vacancies/process/', headers={'Content-Type': 'application/json',
									  'Authorization': 'Token {}'.format('9c1a7ec45beaa34c3059e9c6e226142fe4606741')})
	data = vacancy.json()

	# try:
	#     item = paginator.page(page)
	# except PageNotAnInteger:
	#     item = paginator.page(1)
	# except EmptyPage:
	#     item = paginator.page(paginator.num_pages)

		# data_kiosk = requests.get('http://127.0.0.1:8000/api/created_post/directoryviews/', headers={'Content-Type': 'application/json',
		#                                         'Authorization': 'Token {}'.format('9c30ef9e353f25cd777ff1c805e3d9683b43f682')})

		# info_kiosk_data = data_kiosk.json()
		# print(info_kiosk_data[0]['id'])
	


 
	# token = Token.objects.create(user_id=1)
	# print("WAW",token.key)

	context = {
		'value': data,
		'date': current_date,
		#   'test':data_kiosk.json(),
	}
	return render(request, 'vacancies.html', context)


def IECMaterialsFiles(request):
	data =  iecMaterial.objects.filter().first()
	
	context = {
		  'files': iecMaterial.objects.all(),
		  'firstData': data, #GET THE FIRST ID NUMBER IN IEC MATERIAL
	}
	return render(request, 'iecmaterial.html', context)