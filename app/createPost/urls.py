from django.urls import path

from .views import create_post, post_data, upload_picture, modalForMap, modalForLocation, removeLocation, deletePostedData, \
                    create_directory, modalForDirectoryList, modalViewingDirectoryList, create_satelliteOffices, remove_information, \
                    createIECMaterial

urlpatterns = [
    path('post/', create_post, name='create_post'),
    path('post_data/<int:pk>/', post_data, name='post_data'),
    path('upload_picture/',upload_picture, name='upload_picture'),
    path('modalForMap/<int:pk>/', modalForMap, name='modalForMap'),
    path('modalForLocation/<int:pk>/', modalForLocation, name='modalForRequirements'),
    path('removeLocation/', removeLocation,name='removeLocation'),
    path('deletePostedData/', deletePostedData, name='deletePostedData'),

    #DIRECTORY
    path('create_directory/', create_directory, name='create_directory'),
    path('modalForDirectoryList/<int:pk>/', modalForDirectoryList,name='modalForDirectoryList'),
    path('modalViewingDirectoryList/<int:pk>', modalViewingDirectoryList, name='modalViewingDirectoryList'),

    #SALLITEOFIFCES
    path('create_satelliteOffices/', create_satelliteOffices, name='create_satelliteOffices'),
    path('remove_information', remove_information, name='remove_information'),

    #IECMaterial
    path('createIECMaterial', createIECMaterial, name='createIECMaterial')
]