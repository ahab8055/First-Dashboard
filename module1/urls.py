from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login', logedin, name='logedin'),
    path('adminregistration', adminregistration, name='adminregistration'),
    path('search', search, name='search'),
    path('logedout', logedout, name='logedout'),
    path('index', index, name='index'),
    path('studentregistration', studentregistration, name='studentregisteration'),
    path('teacherregistration', teacherregistration, name='teacherregistration'),
    path('detail/<int:id>', detail, name='detail'),
    path('edit/<int:id>/<str:data>', edit, name='edit'),
    path('setting', setting, name='setting'),
    path('admindetail/<str:usr>', admindetail, name='admindetail'),
    path('delete/<int:id>', delete, name='delete'),
    path('deleteadmin/<str:usr>', deleteadmin, name='deleteadmin'),
    path('csvgenration/<int:id>/<str:data>', csvgenration, name='csvgenration'),
    path('detailteacher/<str:cnic>', detailteacher, name='detailteacher'),
    path('editteacher/<str:cnic>', editteacher, name='editteacher'),
    path('deleteteacher/<str:cnic>', deleteteacher, name='deleteteacher')
]
