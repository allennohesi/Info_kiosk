from django.urls import include, path


urlpatterns = [
    path('user/', include('api.users.urls')),
    path('created_post/', include('api.created_post.urls')),
]