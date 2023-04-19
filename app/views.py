from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from app.createPost.models import createdPost, uploadfile, upload_profile, location_picture, createFeedback
from django.views.decorators.csrf import csrf_exempt

def landingpage(request):
    context = {
         'feedback': createFeedback.objects.all().order_by('-id')
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
    print("TEST")
    for row in data:
         print("TEST RANI",row.get_location)
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
