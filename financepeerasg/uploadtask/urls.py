from django.urls import path
from . import views

urlpatterns = [
    path('', views.userdata, name='home'),
    path('usersdata', views.getall, name='usersdata')
]
