from django.contrib import admin
from django.urls import path,include
from .views import *
app_name = 'fee'
urlpatterns = [
    path('middelfee', middelfee, name='middelfee'),
    path('ninethfee', ninethfee, name='ninethfee'),
    path('tenthfee', tenthfee, name='tenthfee'),
    path('firstyearfee', firstyearfee, name='firstyearfee'),
    path('secondyearfee', secondyearfee, name='secondyearfee'),
    path('bafee', bafee, name='bafee'),
    path('bscfee', bscfee, name='bscfee'),
    path('bcomfee', bcomfee, name='bcomfee'),
    path('monthlyfee', monthlyfee, name='monthlyfee'),
    path('annualfee', annualfee, name='annualfee'),
    path('persubjectfee', persubjectfee, name='persubjectfee'),
    path('pendingfee', pendingfee, name='pendingfee'),
    path('csvgenration/<str:data>/<str:month>/<str:year>',csvgenrationfee,name='csvgenrationfee')
]