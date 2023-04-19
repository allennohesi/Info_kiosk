from rest_framework import serializers

from app.createPost.models import createdPost, createFeedback, createDirectory, createDirectorySwad


class createdPostSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_fullname', read_only=True)
    date_created = serializers.DateTimeField(format="%b %d, %Y - %H:%M %p", read_only=True)

    class Meta:
        model = createdPost
        fields = '__all__'

class createFeedbackSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format="%b %d, %Y - %H:%M %p", read_only=True)

    class Meta:
        model = createFeedback
        fields = '__all__'

#DIRECTORY
class createDirectorySerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_fullname', read_only=True)
    date_created = serializers.DateTimeField(format="%b %d, %Y - %H:%M %p", read_only=True)

    class Meta:
        model = createDirectory
        fields = '__all__'

#SATELLITEOFFICES
class createDirectorySwadSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_fullname', read_only=True)
    date_created = serializers.DateTimeField(format="%b %d, %Y - %H:%M %p", read_only=True)

    class Meta:
        model = createDirectorySwad
        fields = '__all__'
