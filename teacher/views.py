from django.shortcuts import render,redirect
import datetime
from django.http import HttpResponse
import csv
from .models import *
def middelteacher(request):
    if request.user.is_authenticated:
        data = classteacher('Middel')
        return render(request,'middelteacher.html',{'data':data})
    else:
        return redirect('logedin')
def ninethteacher(request):
    if request.user.is_authenticated:
        data = classteacher('Nineth')
        return render(request,'ninethteacher.html',{'data':data})
    else:
        return redirect('logedin')
def tenthteacher(request):
    if request.user.is_authenticated:
        data = classteacher('Tenth')
        return render(request,'tenthteacher.html',{'data':data})
    else:
        return redirect('logedin')
def firstyearteacher(request):
    if request.user.is_authenticated:
        data = classteacher('First year')
        return render(request,'firstyearteacher.html',{'data':data})
    else:
        return redirect('logedin')
def secondyearteacher(request):
    if request.user.is_authenticated:
        data = classteacher('Second year')
        return render(request,'secondyearteacher.html',{'data':data})
    else:
        return redirect('logedin')
def bateacher(request):
    if request.user.is_authenticated:
        data = classteacher('Bachelors')
        return render(request,'bateacher.html',{'data':data})
    else:
        return redirect('logedin')
def bscteacher(request):
    if request.user.is_authenticated:
        data = classteacher('Bsc')
        return render(request,'bscteacher.html',{'data':data})
    else:
        return redirect('logedin')
def bcomteacher(request):
    if request.user.is_authenticated:
        data = classteacher('Bcom')
        return render(request,'bcomteacher.html',{'data':data})
    else:
        return redirect('logedin')
def science(request):
    if request.user.is_authenticated:
        data = subjectteacher('Science')
        return render(request,'science.html',{'data':data})
    else:
        return redirect('logedin')
def arts(request):
    if request.user.is_authenticated:
        data = subjectteacher('Arts')
        return render(request,'arts.html',{'data':data})
    else:
        return redirect('logedin')
def bio(request):
    if request.user.is_authenticated:
        data = subjectteacher('Bio')
        return render(request,'bio.html',{'data':data})
    else:
        return redirect('logedin')
def physics(request):
    if request.user.is_authenticated:
        data = subjectteacher('Physics')
        return render(request,'physics.html',{'data':data})
    else:
        return redirect('logedin')
def chemistry(request):
    if request.user.is_authenticated:
        data = subjectteacher('Chemistry')
        return render(request,'chemistry.html',{'data':data})
    else:
        return redirect('logedin')
def computer(request):
    if request.user.is_authenticated:
        data = subjectteacher('Computer')
        return render(request,'computer.html',{'data':data})
    else:
        return redirect('logedin')
def english(request):
    if request.user.is_authenticated:
        data = subjectteacher('English')
        return render(request,'english.html',{'data':data})
    else:
        return redirect('logedin')
def urdu(request):
    if request.user.is_authenticated:
        data = subjectteacher('Urdu')
        return render(request,'urdu.html',{'data':data})
    else:
        return redirect('logedin')
def islamiyat(request):
    if request.user.is_authenticated:
        data = subjectteacher('Islamiyat')
        return render(request,'islamiyat.html',{'data':data})
    else:
        return redirect('logedin')
def pakstudies(request):
    if request.user.is_authenticated:
        data = subjectteacher('Pakstudies')
        return render(request,'pakstudies.html',{'data':data})
    else:
        return redirect('logedin')
def stat(request):
    if request.user.is_authenticated:
        data = subjectteacher('Stat')
        return render(request,'stat.html',{'data':data})
    else:
        return redirect('logedin')
def economics(request):
    if request.user.is_authenticated:
        data = subjectteacher('Economics')
        return render(request,'economics.html',{'data':data})
    else:
        return redirect('logedin')
def accounting(request):
    if request.user.is_authenticated:
        data = subjectteacher('Accounting')
        return render(request,'accounting.html',{'data':data})
    else:
        return redirect('logedin')
def commerce(request):
    if request.user.is_authenticated:
        data = subjectteacher('Commerce')
        return render(request,'commerce.html',{'data':data})
    else:
        return redirect('logedin')
def banking(request):
    if request.user.is_authenticated:
        data = subjectteacher('Banking')
        return render(request,'banking.html',{'data':data})
    else:
        return redirect('logedin')
def teacherfee(request):
    if request.user.is_authenticated:
        return render(request,'teacherfee.html')
    else:
        return redirect('logedin')
def teachertimeing(request):
    if request.user.is_authenticated:
        return render(request,'teachertiming.html')
    else:
        return redirect('logedin')
def subjectteacher(subj):
    return Teacher_Info.objects.filter(tea_subj__subjects__contains=subj).values('teacher_name', 'teacher_fname',
                                                                               'tea_class__clas', 'teacher_phone','teacher_cnic')
def classteacher(clas):
    return Teacher_Info.objects.filter(tea_class__clas__contains=clas).values('teacher_name', 'teacher_fname',
                                                                              'tea_subj__subjects', 'pay','teacher_cnic')
def all(request):
    if request.user.is_authenticated:
        data = Teacher_Info.objects.all().values('teacher_name','teacher_fname','teacher_cnic','teacher_addres','doj','pay').order_by('doj')
        num = data.count()
        return render(request,'allteachers.html',{'data':data,'num':num})
    else:
        return redirect('logedin')
def teachercsv(request):
    if request.user.is_authenticated:
        newdata = Teacher_Info.objects.all().values('teacher_name', 'teacher_fname', 'teacher_cnic', 'teacher_addres','doj', 'pay','teacher_phone').order_by('doj')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=Teachers.csv'
        writer = csv.writer(response)
        writer.writerow(['Teacher_name', 'Father_name', 'Cnic', 'Addres', 'Contact #', 'Doj','Pay'])
        for cdr in newdata:
            writer.writerow([cdr['teacher_name'], cdr['teacher_fname'], cdr['teacher_cnic'], cdr['teacher_addres'], cdr['teacher_phone'], cdr['doj'], cdr['pay']])
        return response
    else:
        return redirect('logedin')