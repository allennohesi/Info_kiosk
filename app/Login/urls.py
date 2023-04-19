from django.urls import path

from .views import login, dashboard, logout

urlpatterns = [
    path('', login, name='login'),
    path('home/', dashboard, name='home'),
    path('logout/', logout, name='logout')
]