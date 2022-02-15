from django.shortcuts import render,redirect
from module1.models import *
from django.http import HttpResponse
import csv
# Create your views here.
def middel(request):
    if request.user.is_authenticated:
        data,num = classdata('Middel')
        return render(request,'middel.html',{'data':data,'num':num})
    else:
        return redirect('logedin')
def nineth(request):
    if request.user.is_authenticated:
        data,num = classdata('Nineth')
        return render(request, 'nineth.html', {'data': data,'num':num})
    else:
        return redirect('logedin')
def tenth(request):
    if request.user.is_authenticated:
        data,num = classdata('Tenth')
        return render(request,'tenth.html',{'data':data,'num':num})
    else:
        return redirect('logedin')
def firstyear(request):
    if  request.user.is_authenticated:
        data,num = classdata('First year')
        return render(request,'firstyear.html',{'data':data,'num':num})
    else:
        return redirect('logedin')
def secondyear(request):
    if request.user.is_authenticated:
        data,num = classdata('Second year')
        return render(request,'secondyear.html',{'data':data,'num':num})
    else:
        return redirect('logedin')
def ba(request):
    if request.user.is_authenticated:
        data,num = classdata('Bachelors')
        return render(request,'ba.html',{'data':data,'num':num})
    else:
        return redirect('logedin')
def bsc(request):
    if request.user.is_authenticated:
        data,num = classdata('Bsc')
        return render(request,'bsc.html',{'data':data,'num':num})
    else:
        return redirect('logedin')
def bcom(request):
    if request.user.is_authenticated:
        data,num = classdata('Bcom')
        return render(request,'bcom.html',{'data':data,'num':num})
    else:
        return redirect('logedin')
def classdata(clas):
    data = Student_detail.objects.filter(clas=clas).values('roll_id', 'subject', 'clas_fee','roll__father_name', 'roll__phone','roll__student_name').order_by('roll')
    num = data.count()
    return data,num
def all(request):
    if request.user.is_authenticated:
        """ data = studentinfo.objects.all().values('roll','student_name','father_name','phone','addres','student_detail__clas').order_by('roll')
        num = data.count() """
        data = 'data'
        num = 'num'
        return render(request,'allstudents.html',{'data':data,'num':num})
    else:
        return redirect('logedin')
def csvgenrationstudent(request,data):
    if request.user.is_authenticated:
        if data == 'all':
            newdata = studentinfo.objects.all().values('roll', 'student_name', 'father_name', 'phone', 'addres','student_detail__clas').order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Students.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Addres','Clas'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['student_name'], cdr['father_name'],cdr['phone'],cdr['addres'],cdr['student_detail__clas']])
            return response
        elif data == 'Middel':
            newdata = studentinfo.objects.filter(student_detail__clas=data).values('roll', 'student_name', 'father_name', 'phone', 'addres','student_detail__clas').order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Middel.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Addres','Clas'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['student_name'], cdr['father_name'],cdr['phone'],cdr['addres'],cdr['student_detail__clas']])
            return response
        elif data == 'Nineth':
            newdata = studentinfo.objects.filter(student_detail__clas=data).values('roll', 'student_name', 'father_name', 'phone', 'addres','student_detail__clas').order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Nineth.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Addres','Clas'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['student_name'], cdr['father_name'],cdr['phone'],cdr['addres'],cdr['student_detail__clas']])
            return response
        elif data == 'Tenth':
            newdata = studentinfo.objects.filter(student_detail__clas=data).values('roll', 'student_name', 'father_name', 'phone', 'addres','student_detail__clas').order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Tenth.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Addres','Clas'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['student_name'], cdr['father_name'],cdr['phone'],cdr['addres'],cdr['student_detail__clas']])
            return response
        elif data == 'Firstyear':
            newdata = studentinfo.objects.filter(student_detail__clas=data).values('roll', 'student_name', 'father_name', 'phone', 'addres','student_detail__clas').order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Firstyear.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Addres','Clas'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['student_name'], cdr['father_name'],cdr['phone'],cdr['addres'],cdr['student_detail__clas']])
            return response
        elif data == 'Secondyear':
            newdata = studentinfo.objects.filter(student_detail__clas=data).values('roll', 'student_name', 'father_name', 'phone', 'addres','student_detail__clas').order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Secondyear.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Addres','Clas'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['student_name'], cdr['father_name'],cdr['phone'],cdr['addres'],cdr['student_detail__clas']])
            return response
        elif data == 'Ba':
            newdata = studentinfo.objects.filter(student_detail__clas='Bachelors').values('roll', 'student_name', 'father_name', 'phone', 'addres','student_detail__clas').order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Ba.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Addres','Clas'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['student_name'], cdr['father_name'],cdr['phone'],cdr['addres'],cdr['student_detail__clas']])
            return response
        elif data == 'Bsc':
            newdata = studentinfo.objects.filter(student_detail__clas=data).values('roll', 'student_name', 'father_name', 'phone', 'addres','student_detail__clas').order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Bsc.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Addres','Clas'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['student_name'], cdr['father_name'],cdr['phone'],cdr['addres'],cdr['student_detail__clas']])
            return response
        else:
            newdata = studentinfo.objects.filter(student_detail__clas=data).values('roll', 'student_name', 'father_name', 'phone', 'addres','student_detail__clas').order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Bcom.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Addres','Clas'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['student_name'], cdr['father_name'],cdr['phone'],cdr['addres'],cdr['student_detail__clas']])
            return response
    else:
        return redirect('logedin')