
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from app.views import indexData, modalforData, landingpage, proceed, FrontlineServices, NonFrontlineServices, uploadFeedback, deletefeedback, \
                modalforpdfviewing, vacancies
urlpatterns = [
    path('login/', include('app.Login.urls')),
    path('user/', include('app.user_registration.urls')),
    path('create/',include('app.createPost.urls')),
    path('api/', include('api.urls')),

    # path('', index, name='index'),
    path('', landingpage, name='landingpage'),
    path('proceed/', proceed,name='proceed'),
    path('posted/data/frontline/', FrontlineServices, name='FrontlineServices'),
    path('posted/data/NonFrontline/', NonFrontlineServices, name='NonFrontlineServices'),
    path('uploadFeedback/', uploadFeedback,name='uploadFeedback'),
    path('deletefeedback/', deletefeedback, name='deletefeedback'),
    path('vacancies/', vacancies, name='vacancies'),

    path('modalforData/<int:pk>/', modalforData, name='modalforData'),
    path('index/data/<int:pk>/', indexData, name='indexData'),
    path('modalforpdfviewing/<int:pk>/', modalforpdfviewing, name='modalforpdfviewing')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
