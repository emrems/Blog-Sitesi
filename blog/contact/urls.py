
from django.urls import path
from django.contrib import admin
from .views import emailView



urlpatterns = [
    path('', emailView, name='contact'),
   

]
