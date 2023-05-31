from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.created_post.serializers import createdPostSerializer, createFeedbackSerializer, createDirectorySerializer, \
			createDirectorySwadSerializer, createdPostDataSerializer

from app.createPost.models import createdPost, createFeedback, createDirectory, createDirectorySwad, uploadfile


class createdViews(generics.ListAPIView):
	permission_classes = [IsAuthenticated]
	queryset = createdPost.objects.all()
	serializer_class = createdPostSerializer

class createdFeedBackViews(generics.ListAPIView):
	permission_classes = [IsAuthenticated]
	queryset = createFeedback.objects.all()
	serializer_class = createFeedbackSerializer


# DIRECTORY
class createDirectoryViews(generics.ListAPIView):
	# permission_classes = [IsAuthenticated]
	queryset = createDirectory.objects.all()
	serializer_class = createDirectorySerializer

# SWAD DIRECTORY
class createDirectorySwadViews(generics.ListAPIView):
	# permission_classes = [IsAuthenticated]
	queryset = createDirectorySwad.objects.all()
	serializer_class = createDirectorySwadSerializer

# ALL FILES
class createdPostDataViews(generics.ListAPIView):
	queryset = uploadfile.objects.filter(file_ext=".pdf")
	serializer_class = createdPostDataSerializer