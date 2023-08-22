from django.contrib import admin
from django.urls import path, include

from main.views import contacts, home

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('home/', home, name='home')
]
