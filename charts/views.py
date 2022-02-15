from django.shortcuts import render,redirect
import datetime
from module1.models import *
def tables(request):
    if request.user.is_authenticated:
        return render(request,'tables.html')
    else:
        return redirect('logedin')
def typography(request):
    if request.user.is_authenticated:
        return render(request,'typography.html')
    else:
        return redirect('logedin')
def more_notifications(request):
    if request.user.is_authenticated:
        return render(request,'more_notifications.html')
    else:
        return redirect('logedin')
def forms_validations(request):
    if request.user.is_authenticated:
        return render(request,'forms_validation.html')
    else:
        return redirect('logedin')
def pages_offline(request):
    if request.user.is_authenticated:
        return render(request,'pages_offline.html')
    else:
        return redirect('logedin')
def pages_uc(request):
    if request.user.is_authenticated:
        return render(request,'pages_uc.html')
    else:
        return redirect('logedin')
def gallery2(request):
    if request.user.is_authenticated:
        return render(request,'gallery2.html')
    else:
        return redirect('logedin')
def blank(request):
    if request.user.is_authenticated:
        return render(request,'blank.html')
    else:
        return redirect('logedin')
def grid(request):
    if request.user.is_authenticated:
        return render(request,'grid.html')
    else:
        return redirect('logedin')
def maps(request):
    if request.user.is_authenticated:
        return render(request,'maps.html')
    else:
        return redirect('logedin')
def feechart(request):
    if request.user.is_authenticated:
        return render(request,'feechart.html')
    else:
        return redirect('logedin')
def progresschart(request):
    if request.user.is_authenticated:
        return render(request,'progresschart.html')
    else:
        return redirect('logedin')
def profitchart(request):
    if request.user.is_authenticated:
        return render(request,'profitchart.html')
    else:
        return redirect('logedin')
def attendancechart(request):
    if request.user.is_authenticated:
        return render(request,'attendancechart.html')
    else:
        return redirect('logedin')