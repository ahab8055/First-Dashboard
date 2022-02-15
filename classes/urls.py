from django.contrib import admin
from django.urls import path,include
from .views import *
app_name = 'class'
urlpatterns = [
path('middel',  middel, name='middel'),
    path('nineth',  nineth, name='nineth'),
    path('tenth',  tenth, name='tenth'),
    path('firstyear',  firstyear, name='firstyear'),
    path('secondyear',  secondyear, name='secondyear'),
    path('ba', ba, name='ba'),
    path('bsc', bsc, name='bsc'),
    path('bcom', bcom, name='bcom'),
    path('students',all,name='students'),
    path('csvgenration/<str:data>',csvgenrationstudent,name='csvgenrationstudent')
]