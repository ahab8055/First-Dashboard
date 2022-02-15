from django.contrib import admin
from django.urls import path,include,re_path
from .views import *
app_name = 'attendance'
urlpatterns = [
    path('middelattendance', middelattendance, name='middelattendance'),
    path('ninethattendance', ninethattendance, name='ninethattendance'),
    path('tenthattendance', tenthattendance, name='tenthattendance'),
    path('firstyearattendance', firstyearattendance, name='firstyearattendance'),
    path('secondyearattendance', secondyearattendance, name='secondyearattendance'),
    path('baattendance', baattendance, name='baattendance'),
    path('bscattendance', bscattendance, name='bscattendance'),
    path('bcomattendance', bcomattendance, name='bcomattendance'),
    path('takeattendance',takeattendance,name='takeattendance'),
    re_path(r'^attendancecsv/(?P<date>\d{4}-\d{2}-\d{2})/(?P<data>[A-Z][a-z]{1,15})$',attendancecsv,name='attendancecsv')
]