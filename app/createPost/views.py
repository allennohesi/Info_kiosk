
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from app.models import AuthUser
from app.createPost.models import createdPost, uploadfile, upload_profile, location_picture, createLocation, createDirectory, createDirectoryPicture, \
							createDirectorySwad, iecMaterial
import os
from django.views.decorators.csrf import csrf_exempt


@login_required
def create_post(request):
	if request.method == "POST":
		create_post = createdPost.objects.create(
			title=request.POST.get('title_post'),
			created_by_id=request.user.id,
			url=request.POST.get('url') if request.POST.get('url') else None,
			remarks=request.POST.get('remarks'),
			status=True if request.POST.get('is_active') else False,
			services_type=request.POST.get('services')
		)
		return JsonResponse({'msg': 'You successfully saved the data'})
	
	return render(request, 'createPost/create_post.html')

@login_required
def upload_picture(request):
	if request.method == "POST":
		upload_profile.objects.filter(created_id=request.POST.get('postID')).delete()
		upload_pict = upload_profile.objects.create(
			created_id=request.POST.get('postID'),
			profile_pict=request.FILES.get('file')
		)
		return JsonResponse({'msg': 'You successfully uploaded your picture'})

@login_required
def post_data(request, pk):
	if request.method == "POST":
		split_tup = os.path.splitext(str(request.FILES.get('upload')))
		file_extension = split_tup[1]
		post_data = uploadfile.objects.create(
			title_post=request.POST.get('title_post'),
			title_text=request.POST.get('title'),
			description_post=request.POST.get('description_post'),
			file_upload=request.FILES.get('upload'),
			title_id=pk,
			file_ext=file_extension,
			user_id=request.user.id
		)
		return JsonResponse({'msg': 'You successfully post data'})
	uploaded = uploadfile.objects.filter(title_id=pk).order_by('-id')
	profile = upload_profile.objects.filter(created_id=pk).first()
	
	context = {
		'information': createdPost.objects.filter(id=pk).first(),
		'data': uploaded,
		'template_profile': profile
	}
	return render(request, 'createPost/post_data.html', context)

@login_required
def modalForMap(request,pk):
	if request.method == "POST":
		upload_pict = location_picture.objects.create(
			created_id=pk,
			user_id=request.user.id,
			photo=request.FILES.get('photo'),
		)
		return JsonResponse({'msg': 'You successfully updated the map'})
	context = {
		'information': createdPost.objects.filter(id=pk).first(),
		'location_data': location_picture.objects.filter(created_id=pk).first()
	}
	return render(request, 'createPost/upload_locationModal.html', context)

@login_required
def modalForLocation(request,pk):
	if request.method == "POST":
		upload_location = createLocation.objects.create(
			created_id=pk,
			user_id=request.user.id,
			location=request.POST.get('requirements'),
		)
		return JsonResponse({'msg': 'You successfully added location'})
	context = {
		'information': createdPost.objects.filter(id=pk).first(),
		'requirements': createLocation.objects.filter(created_id=pk).all()
	}
	return render(request, 'createPost/upload_locationDetails.html', context)

@csrf_exempt
def removeLocation(request):
	if request.method == "POST":
		data = createLocation.objects.filter(id=request.POST.get('id')).delete()
	return JsonResponse({'data': 'success'})

@csrf_exempt
def deletePostedData(request):
	if request.method == "POST":
		print("THIS IS TEST", request.POST.get('id'))
		uploadfile.objects.filter(id=request.POST.get('id')).delete()
	return JsonResponse({'data': 'success'})

#CREATE DIRECTORY
@login_required
def create_directory(request):
	if request.method == "POST":
		create_post = createDirectory.objects.create(
			name=request.POST.get('Name'),
			position=request.POST.get('Position'),
			email=request.POST.get('Email'),
			information=request.POST.get('Information'),
			created_by_id=request.user.id,
		)
		return JsonResponse({'msg': 'You successfully added directory'})
	
	return render(request, 'createPost/create_directory.html')

@login_required
def modalForDirectoryList(request,pk):
	if request.method == "POST":
		upload_pict = createDirectoryPicture.objects.create(
			directory_id=pk,
			photo=request.FILES.get('photo'),
		)
		return JsonResponse({'msg': 'You successfully updated the map'})
	
	context = {
		'data': createDirectory.objects.filter(id=pk).first(),
		'dataPicture': createDirectoryPicture.objects.filter(directory_id=pk).first()
	}
	return render(request, 'createPost/modalDirectory.html', context)

def modalViewingDirectoryList(request,pk):
	print("THIS IS FOR VIEWING ONLY", pk)
	context = {
		'data': createDirectory.objects.filter(id=pk).first(),
		'dataPicture': createDirectoryPicture.objects.filter(directory_id=pk).first()
	}
	return render(request, 'createPost/modalViewingDirectory.html', context)

#CreateSatelliteOffices
@login_required
def create_satelliteOffices(request):
	if request.method == "POST":
		create_post = createDirectorySwad.objects.create(
			swad_team=request.POST.get('swadteam'),
			address=request.POST.get('address'),
			contact_no=request.POST.get('contactno'),
			email=request.POST.get('email'),
			created_by_id=request.user.id,
		)
		return JsonResponse({'msg': 'You successfully added Swad list'})
	
	return render(request, 'createPost/create_satelliteOffices.html')

@csrf_exempt
def remove_information(request):
	if request.method == "POST":
		print("test ", request.POST.get('id'))
		createDirectorySwad.objects.filter(id=request.POST.get('id')).delete()
	return JsonResponse({'data': 'success'})

#create IEC Material

@login_required
def createIECMaterial(request):
	if request.method == "POST":
		create_post = iecMaterial.objects.create(
			title=request.POST.get('title'),#ForTabNameOnly
			title_IECMaterial=request.POST.get('title_IECMaterial'),
			description=request.POST.get('description'),
			video=request.FILES.get('file')
		)
		return JsonResponse({'msg': 'You successfully added IEC Material'})
	
	context = {
		'files': iecMaterial.objects.all(),
		
	}
	return render(request, 'createPost/create_IECmaterial.html', context)