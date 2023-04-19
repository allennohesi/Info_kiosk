from django.urls import path

from .views import list_users,edit

urlpatterns = [
    path('list_users/', list_users, name='list_users'),
    path('edit/<int:pk>',edit,name='edit')
]