from django.contrib import admin
from django.urls import path,include
from .views import *
app_name = 'charts'
urlpatterns = [
    path('maps',  maps, name='maps'),
    path('blank',  blank, name='blank'),
    path('more_notifications', more_notifications , name='more_notifications'),
    path('forms_validations', forms_validations, name='forms_validations'),
    path('pages_offline', pages_offline, name='pages_offline'),
    path('pages_uc', pages_uc, name='pages_uc'),
    path('gallery2', gallery2, name='gallery2'),
    path('grid', grid, name='grid'),
    path('tables', tables, name='tables'),
    path('typography', typography, name='typography'),
    path('feechart', feechart, name='feechart'),
    path('progresschart', progresschart, name='progresschart'),
    path('profitchart', profitchart, name='profitchart'),
    path('attendancechart', attendancechart, name='attendancechart'),
]