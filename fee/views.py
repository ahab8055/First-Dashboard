from django.shortcuts import render,redirect
import datetime
from django.db.models import Sum
from .models import *
from module1.views import monthname
from .form import *
import csv
from django.http import HttpResponse
from django.urls import reverse
def middelfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mon = request.POST['month']
            year = request.POST['year']
            dat = str(mon) + "-" + str(year)
            data , month , form1, form2,num,num1 = feedata(dat,'Middel')
            return render(request,'middelfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
        else:
            year = str(datetime.now().year)
            mon = str(datetime.now().month)
            dat = mon + '-' + year
            data , month , form1, form2,num,num1 = feedata(dat,'Middel')
            return render(request, 'middelfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
    else:
        return redirect('logedin')
def ninethfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mon = request.POST['month']
            year = request.POST['year']
            dat = str(mon) + "-" + str(year)
            data, month, form1, form2,num,num1 = feedata(dat, 'Nineth')
            return render(request, 'ninethfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
        else:
            year = str(datetime.now().year)
            mon = str(datetime.now().month)
            dat = mon + '-' + year
            data, month, form1, form2,num,num1 = feedata(dat, 'Nineth')
            return render(request, 'ninethfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
    else:
        return redirect('logedin')
def tenthfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mon = request.POST['month']
            year = request.POST['year']
            dat = str(mon) + "-" + str(year)
            data , month , form1, form2,num,num1 = feedata(dat,'Tenth')
            return render(request, 'tenthfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
        else:
            year = str(datetime.now().year)
            mon = str(datetime.now().month)
            dat = mon + '-' + year
            data , month , form1, form2,num,num1 = feedata(dat,'Tenth')
            return render(request, 'tenthfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
    else:
        return redirect('logedin')
def firstyearfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mon = request.POST['month']
            year = request.POST['year']
            dat = str(mon) + "-" + str(year)
            data , month , form1, form2,num,num1 = feedata(dat,'First year')
            return render(request, 'firstyearfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
        else:
            year = str(datetime.now().year)
            mon = str(datetime.now().month)
            dat = mon + '-' + year
            data , month , form1, form2,num,num1 = feedata(dat,'First year')
            return render(request, 'firstyearfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
    else:
        return redirect('logedin')
def secondyearfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mon = request.POST['month']
            year = request.POST['year']
            dat = str(mon) + "-" + str(year)
            data , month , form1, form2,num,num1 = feedata(dat,'Second year')
            return render(request, 'secondyearfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
        else:
            year = str(datetime.now().year)
            mon = str(datetime.now().month)
            dat = mon + '-' + year
            data , month , form1, form2,num,num1 = feedata(dat,'Second year')
            return render(request, 'secondyearfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
    else:
        return redirect('logedin')
def bafee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mon = request.POST['month']
            year = request.POST['year']
            dat = str(mon) + "-" + str(year)
            data , month , form1, form2,num,num1 = feedata(dat,'Bachelors')
            return render(request, 'bafee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
        else:
            year = str(datetime.now().year)
            mon = str(datetime.now().month)
            dat = mon + '-' + str(datetime.now().year)
            data , month , form1, form2,num,num1 = feedata(dat,'Bachelors')
            return render(request, 'bafee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
    else:
        return redirect('logedin')
def bscfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mon = request.POST['month']
            year = request.POST['year']
            dat = str(mon) + "-" + str(year)
            data , month , form1, form2,num,num1 = feedata(dat,'Bsc')
            return render(request, 'bscfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
        else:
            year = str(datetime.now().year)
            mon = str(datetime.now().month)
            dat = mon + '-' + year
            data , month , form1, form2,num,num1 = feedata(dat,'Bsc')
            return render(request, 'bscfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
    else:
        return redirect('logedin')
def bcomfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mon = request.POST['month']
            year = request.POST['year']
            dat = str(mon) + "-" + str(year)
            data , month , form1, form2,num,num1 = feedata(dat,'Bcom')
            return render(request, 'bcomfee.html', {'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
        else:
            year = str(datetime.now().year)
            mon = str(datetime.now().month)
            dat = mon + '-' + year
            data , month , form1, form2,num,num1 = feedata(dat,'Bcom')
            return render(request, 'bcomfee.html', {'data': data, 'month': month, 'form': form1,'form2':form2,'year':year,'num':num,'num1':num1,'mon':mon})
    else:
        return redirect('logedin')
def monthlyfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = request.POST['month']
            year = request.POST['year']
            dat = str(dat) + "-" + str(year)
            context = {
                'Middel': [ppfee(dat,'Middel','Paid'),ppfee(dat,'Middel','Pending')],
                'Nineth': [ppfee(dat,'Nineth','Paid'),ppfee(dat,'Nineth','Pending')],
                'Tenth': [ppfee(dat,'Tenth','Paid'),ppfee(dat,'Tenth','Pending')],
                'First year': [ppfee(dat,'First year','Paid'),ppfee(dat,'First year','Pending')],
                'Second year': [ppfee(dat,'Second year','Paid'),ppfee(dat,'Second year','Pending')],
                'B.A': [ppfee(dat,'Bachelors','Paid'),ppfee(dat,'Bachelors','Pending')],
                'Bsc': [ppfee(dat,'Bsc','Paid'),ppfee(dat,'Bsc','Pending')],
                'Bcom': [ppfee(dat,'Bcom','Paid'),ppfee(dat,'Bcom','Pending')],
            }
            month = monthname(dat[:2])
            form1 = fee_date()
            form2 = fee_year()
            return render(request, 'monthlyfee.html', {'data': context, 'form1': form1,'form2':form2,'month':month,'year':year})
        else:
            year = str(datetime.now().year)
            dat = str(datetime.now().month) + "-" + year
            context = {
                'Middel': [ppfee(dat, 'Middel', 'Paid'), ppfee(dat, 'Middel', 'Pending')],
                'Nineth': [ppfee(dat, 'Nineth', 'Paid'), ppfee(dat, 'Nineth', 'Pending')],
                'Tenth': [ppfee(dat, 'Tenth', 'Paid'), ppfee(dat, 'Tenth', 'Pending')],
                'First year': [ppfee(dat, 'First year', 'Paid'), ppfee(dat, 'First year', 'Pending')],
                'Second year': [ppfee(dat, 'Second year', 'Paid'), ppfee(dat, 'Second year', 'Pending')],
                'B.A': [ppfee(dat, 'Bachelors', 'Paid'), ppfee(dat, 'Bachelors', 'Pending')],
                'Bsc': [ppfee(dat, 'Bsc', 'Paid'), ppfee(dat, 'Bsc', 'Pending')],
                'Bcom': [ppfee(dat, 'Bcom', 'Paid'), ppfee(dat, 'Bcom', 'Pending')],
            }
            month = monthname(dat[:2])
            form1 = fee_date()
            form2 = fee_year()
            return render(request, 'monthlyfee.html', {'data': context, 'form1': form1,'form2':form2, 'month': month,'year':year})
    else:
        return redirect('logedin')
def annualfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = str(request.POST['year'])
            context = {
                'Middel': [ppfee(dat, 'Middel', 'Paid'), ppfee(dat, 'Middel', 'Pending')],
                'Nineth': [ppfee(dat, 'Nineth', 'Paid'), ppfee(dat, 'Nineth', 'Pending')],
                'Tenth': [ppfee(dat, 'Tenth', 'Paid'), ppfee(dat, 'Tenth', 'Pending')],
                'First year': [ppfee(dat, 'First year', 'Paid'), ppfee(dat, 'First year', 'Pending')],
                'Second year': [ppfee(dat, 'Second year', 'Paid'), ppfee(dat, 'Second year', 'Pending')],
                'B.A': [ppfee(dat, 'Bachelors', 'Paid'), ppfee(dat, 'Bachelors', 'Pending')],
                'Bsc': [ppfee(dat, 'Bsc', 'Paid'), ppfee(dat, 'Bsc', 'Pending')],
                'Bcom': [ppfee(dat, 'Bcom', 'Paid'), ppfee(dat, 'Bcom', 'Pending')],
            }
            form = fee_year()
            return render(request, 'annualfee.html', {'data': context, 'form': form, 'year': dat})
        else:
            dat = str(datetime.now().year)
            context = {
                'Middel': [ppfee(dat, 'Middel', 'Paid'), ppfee(dat, 'Middel', 'Pending')],
                'Nineth': [ppfee(dat, 'Nineth', 'Paid'), ppfee(dat, 'Nineth', 'Pending')],
                'Tenth': [ppfee(dat, 'Tenth', 'Paid'), ppfee(dat, 'Tenth', 'Pending')],
                'First year': [ppfee(dat, 'First year', 'Paid'), ppfee(dat, 'First year', 'Pending')],
                'Second year': [ppfee(dat, 'Second year', 'Paid'), ppfee(dat, 'Second year', 'Pending')],
                'B.A': [ppfee(dat, 'Bachelors', 'Paid'), ppfee(dat, 'Bachelors', 'Pending')],
                'Bsc': [ppfee(dat, 'Bsc', 'Paid'), ppfee(dat, 'Bsc', 'Pending')],
                'Bcom': [ppfee(dat, 'Bcom', 'Paid'), ppfee(dat, 'Bcom', 'Pending')],
            }
            form = fee_year()
            return render(request,'annualfee.html',{'data':context,'form':form,'year':dat})
    else:
        return redirect('logedin')
def persubjectfee(request):
    if request.user.is_authenticated:
        return render(request,'persubjectfee.html')
    else:
        return redirect('logedin')
def pendingfee(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mon = str(request.POST['month'])
            year = str(request.POST['year'])
            dat = mon + '-' + year
            data = Fee_detail.objects.filter(fee_status='Pending', month=dat).values('roll', 'roll__student_name',
                                                                                     'roll__father_name',
                                                                                     'roll__phone').order_by('roll')
            num = data.count()
            month = monthname(dat[:2])
            form1 = fee_date()
            form2 = fee_year()
            return render(request, 'pendingfee.html', {'num':num,'data': data, 'month': month, 'form1': form1,'form2':form2,'year':year,'mon':mon})
        else:
            year = str(datetime.now().year)
            mon = str(datetime.now().month)
            dat = mon + '-' + year
            data = Fee_detail.objects.filter(fee_status='Pending',month=dat).values('roll','roll__student_name','roll__father_name','roll__phone').order_by('roll')
            num = data.count()
            month = monthname(dat[:2])
            form1 = fee_date()
            form2 = fee_year()
            return render(request,'pendingfee.html',{'num':num,'data':data,'month':month,'form1':form1,'form2':form2,'year':year,'mon':mon})
    else:
        return redirect('logedin')
def ppfee(dat,clas,status):
    return Student_detail.objects.filter(roll__fee_detail__month__contains=dat, roll__fee_detail__fee_status__exact=status,
                                  clas=clas).aggregate(Sum('clas_fee'))
def feedata(dat,clas):
    data = Fee_detail.objects.filter(month=dat, roll__student_detail__clas=clas).values('roll','roll__student_name','roll__father_name','roll__phone','fee_status').order_by('roll')
    num = Fee_detail.objects.filter(month=dat, roll__student_detail__clas=clas,fee_status='Paid').values('roll','roll__student_name','roll__father_name','roll__phone','fee_status').count()
    num1 = Fee_detail.objects.filter(month=dat, roll__student_detail__clas=clas, fee_status='Pending').values('roll',
                                                                                                          'roll__student_name',
                                                                                                          'roll__father_name',
                                                                                                          'roll__phone',
                                                                                                          'fee_status').count()
    month = monthname(dat[:2])
    form1 = fee_date()
    form2 = fee_year()
    return data , month , form1,form2,num,num1
def csvgenrationfee(request,data,month,year):
    if request.user.is_authenticated:
        if data == 'Pending':
            dat = str(month) + '-' + year
            newdata = Fee_detail.objects.filter(month=dat,fee_status=data).values('roll_id',
                                                                                                   'roll__student_name',
                                                                                                   'roll__father_name',
                                                                                                   'roll__phone',
                                                                                                   'fee_status',
                                                                                                   'month').order_by(
                'month')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Pendingfee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Fee_Status', 'Month'])
            for cdr in newdata:
                writer.writerow(
                    [cdr['roll_id'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['roll__phone'],
                     cdr['fee_status'], cdr['month']])
            return response
        elif data == 'Middel':
            dat = str(month) + '-' + year
            newdata = Fee_detail.objects.filter(roll__student_detail__clas=data,month=dat).values('roll_id', 'roll__student_name', 'roll__father_name', 'roll__phone', 'fee_status','month').order_by('month')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=MiddelFee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Fee_Status','Month'])
            for cdr in newdata:
                writer.writerow([cdr['roll_id'], cdr['roll__student_name'], cdr['roll__father_name'],cdr['roll__phone'],cdr['fee_status'],cdr['month']])
            return response
        elif data == 'Nineth':
            dat = str(month) + '-' + year
            newdata = Fee_detail.objects.filter(roll__student_detail__clas=data, month=dat).values('roll_id',
                                                                                                   'roll__student_name',
                                                                                                   'roll__father_name',
                                                                                                   'roll__phone',
                                                                                                   'fee_status',
                                                                                                   'month').order_by(
                'month')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=NinethFee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Fee_Status', 'Month'])
            for cdr in newdata:
                writer.writerow(
                    [cdr['roll_id'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['roll__phone'],
                     cdr['fee_status'], cdr['month']])
            return response
        elif data == 'Tenth':
            dat = str(month) + '-' + year
            newdata = Fee_detail.objects.filter(roll__student_detail__clas=data, month=dat).values('roll_id',
                                                                                                   'roll__student_name',
                                                                                                   'roll__father_name',
                                                                                                   'roll__phone',
                                                                                                   'fee_status',
                                                                                                   'month').order_by(
                'month')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=TenthFee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Fee_Status', 'Month'])
            for cdr in newdata:
                writer.writerow(
                    [cdr['roll_id'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['roll__phone'],
                     cdr['fee_status'], cdr['month']])
            return response
        elif data == 'Firstyear':
            dat = str(month) + '-' + year
            newdata = Fee_detail.objects.filter(roll__student_detail__clas=data, month=dat).values('roll_id',
                                                                                                   'roll__student_name',
                                                                                                   'roll__father_name',
                                                                                                   'roll__phone',
                                                                                                   'fee_status',
                                                                                                   'month').order_by(
                'month')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=FirstYearFee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Fee_Status', 'Month'])
            for cdr in newdata:
                writer.writerow(
                    [cdr['roll_id'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['roll__phone'],
                     cdr['fee_status'], cdr['month']])
            return response
        elif data == 'Secondyear':
            dat = str(month) + '-' + year
            newdata = Fee_detail.objects.filter(roll__student_detail__clas=data, month=dat).values('roll_id',
                                                                                                   'roll__student_name',
                                                                                                   'roll__father_name',
                                                                                                   'roll__phone',
                                                                                                   'fee_status',
                                                                                                   'month').order_by(
                'month')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=SecondYearFee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Fee_Status', 'Month'])
            for cdr in newdata:
                writer.writerow(
                    [cdr['roll_id'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['roll__phone'],
                     cdr['fee_status'], cdr['month']])
            return response
        elif data == 'Ba':
            dat = str(month) + '-' + year
            newdata = Fee_detail.objects.filter(roll__student_detail__clas=data, month=dat).values('roll_id',
                                                                                                   'roll__student_name',
                                                                                                   'roll__father_name',
                                                                                                   'roll__phone',
                                                                                                   'fee_status',
                                                                                                   'month').order_by(
                'month')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=BaFee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Fee_Status', 'Month'])
            for cdr in newdata:
                writer.writerow(
                    [cdr['roll_id'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['roll__phone'],
                     cdr['fee_status'], cdr['month']])
            return response
        elif data == 'Bsc':
            dat = str(month) + '-' + year
            newdata = Fee_detail.objects.filter(roll__student_detail__clas=data, month=dat).values('roll_id',
                                                                                                   'roll__student_name',
                                                                                                   'roll__father_name',
                                                                                                   'roll__phone',
                                                                                                   'fee_status',
                                                                                                   'month').order_by(
                'month')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=BscFee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Fee_Status', 'Month'])
            for cdr in newdata:
                writer.writerow(
                    [cdr['roll_id'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['roll__phone'],
                     cdr['fee_status'], cdr['month']])
            return response
        else:
            dat = str(month) + '-' + year
            newdata = Fee_detail.objects.filter(roll__student_detail__clas=data, month=dat).values('roll_id',
                                                                                                   'roll__student_name',
                                                                                                   'roll__father_name',
                                                                                                   'roll__phone',
                                                                                                   'fee_status',
                                                                                                   'month').order_by(
                'month')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=BcomFee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Phone', 'Fee_Status', 'Month'])
            for cdr in newdata:
                writer.writerow(
                    [cdr['roll_id'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['roll__phone'],
                     cdr['fee_status'], cdr['month']])
            return response
    else:
        return redirect('logedin')