from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('login', views.login, name="login"),
]
