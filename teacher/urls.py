from django.contrib import admin
from django.urls import path,include
from .views import *
app_name = 'teacher'
urlpatterns = [
    path('middelteacher', middelteacher, name='middelteacher'),
    path('ninethteacher', ninethteacher, name='ninethteacher'),
    path('tenthteacher', tenthteacher, name='tenthteacher'),
    path('firstyearteacher', firstyearteacher, name='firstyearteacher'),
    path('secondyearteacher', secondyearteacher, name='secondyearteacher'),
    path('bateacher', bateacher, name='bateacher'),
    path('bscteacher', bscteacher, name='bscteacher'),
    path('bcomteacher', bcomteacher, name='bcomteacher'),
    path('science', science, name='science'),
    path('arts', arts, name='arts'),
    path('bio', bio, name='bio'),
    path('physics', physics, name='physics'),
    path('chemistry', chemistry, name='chemistry'),
    path('computer', computer, name='computer'),
    path('english', english, name='english'),
    path('urdu', urdu, name='urdu'),
    path('islamiyat', islamiyat, name='islamiyat'),
    path('pakstudies', pakstudies, name='pakstudies'),
    path('stat', stat, name='stat'),
    path('economics', economics, name='economics'),
    path('accounting', accounting, name='accounting'),
    path('commerce', commerce, name='commerce'),
    path('banking', banking, name='banking'),
    path('teacherfee', teacherfee, name='teacherfee'),
    path('teachertimeing', teachertimeing, name='teachertimeing'),
    path('all',all,name='all'),
    path('csvgenrator',teachercsv,name='teachercsv')
]