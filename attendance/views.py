from django.shortcuts import render,redirect
import datetime
import csv
from  django.contrib import messages
import re
from module1.models import *
from .form import *
from django.http import HttpResponse
# Create your views here.
def classattendance(clas,dat):
    data = Student_detail.objects.filter(clas=clas, roll__student_attendance__date_of_attendance=dat).values(
        'roll', 'roll__student_name', 'roll__father_name', 'roll__student_attendance__attendance',
        'roll__student_attendance__date_of_attendance').order_by('roll')
    num = data.filter(roll__student_attendance__attendance='Present',roll__student_attendance__date_of_attendance=dat).count()
    num1 = data.filter(roll__student_attendance__attendance='Absent',roll__student_attendance__date_of_attendance=dat).count()
    return data,num,num1
def middelattendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = request.POST['date']
            data,num,num1 = classattendance('Middel',dat)
            form = attendancedate()
            return render(request, 'middelattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
        else:
            dat = datetime.now().date()
            data,num,num1 = classattendance('Middel',dat)
            form = attendancedate()
            return render(request,'middelattendance.html',{'data':data,'form':form,'num':num,'num1':num1,'dat':dat})
    else:
        return redirect('logedin')
def ninethattendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = request.POST['date']
            data,num,num1 = classattendance('Nineth', dat)
            form = attendancedate()
            return render(request, 'ninethattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
        else:
            dat = datetime.now().date()
            data,num,num1 = classattendance('Nineth', dat)
            form = attendancedate()
            return render(request, 'ninethattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
    else:
        return redirect('logedin')
def tenthattendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = request.POST['date']
            data,num,num1 = classattendance('Tenth', dat)
            form = attendancedate()
            return render(request, 'tenthattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
        else:
            dat = datetime.now().date()
            data,num,num1 = classattendance('Tenth', dat)
            form = attendancedate()
            return render(request, 'tenthattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
    else:
        return redirect('logedin')
def firstyearattendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = request.POST['date']
            data,num,num1 = classattendance('First year', dat)
            form = attendancedate()
            return render(request, 'firstyearattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
        else:
            dat = datetime.now().date()
            data,num,num1 = classattendance('First Year', dat)
            form = attendancedate()
            return render(request, 'firstyearattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
    else:
        return redirect('logedin')
def secondyearattendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = request.POST['date']
            data = classattendance('Second year', dat)
            form,num,num1 = attendancedate()
            return render(request, 'secondyearattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
        else:
            dat = datetime.now().date()
            data = classattendance('Second year', dat)
            form,num,num1 = attendancedate()
            return render(request, 'secondyearattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
    else:
        return redirect('logedin')
def baattendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = request.POST['date']
            data,num,num1 = classattendance('Bachelors', dat)
            form = attendancedate()
            return render(request, 'baattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
        else:
            dat = datetime.now().date()
            data,num,num1 = classattendance('Bachelors', dat)
            form = attendancedate()
            return render(request, 'baattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
    else:
        return redirect('logedin')
def bscattendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = request.POST['date']
            data,num,num1 = classattendance('Bsc', dat)
            form = attendancedate()
            return render(request, 'bscattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
        else:
            dat = datetime.now().date()
            data,num,num1 = classattendance('Bsc', dat)
            form = attendancedate()
            return render(request, 'bscattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
    else:
        return redirect('logedin')
def bcomattendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dat = request.POST['date']
            data,num,num1 = classattendance('Bcom', dat)
            form = attendancedate()
            return render(request, 'bcomattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
        else:
            dat = datetime.now().date()
            data,num,num1 = classattendance('Bcom', dat)
            form = attendancedate()
            return render(request, 'bcomattendance.html', {'data': data, 'form': form,'num':num,'num1':num1,'dat':dat})
    else:
        return redirect('logedin')
def attendancecsv(request,date,data):
    if request.user.is_authenticated:
        if data == 'Middel':
            newdata = Student_attendance.objects.filter(roll__student_detail__clas=data,date_of_attendance=date).values('roll', 'roll__student_name','roll__father_name', 'attendance', 'date_of_attendance',).order_by('roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Middelattendance.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Attendance_Status', 'Date'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['attendance'], cdr['date_of_attendance']])
            return response
        elif data == 'Nineth':
            newdata = Student_attendance.objects.filter(roll__student_detail__clas=data,
                                                        date_of_attendance=date).values('roll', 'roll__student_name',
                                                                                        'roll__father_name',
                                                                                        'attendance',
                                                                                        'date_of_attendance', ).order_by(
                'roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Ninethattendance.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Attendance_Status', 'Date'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['attendance'],
                                 cdr['date_of_attendance']])
            return response
        elif data == 'Tenth':
            newdata = Student_attendance.objects.filter(roll__student_detail__clas=data,
                                                        date_of_attendance=date).values('roll', 'roll__student_name',
                                                                                        'roll__father_name',
                                                                                        'attendance',
                                                                                        'date_of_attendance', ).order_by(
                'roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Tenthattendance.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Attendance_Status', 'Date'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['attendance'],
                                 cdr['date_of_attendance']])
            return response
        elif data == 'Firstyear':
            newdata = Student_attendance.objects.filter(roll__student_detail__clas=data,
                                                        date_of_attendance=date).values('roll', 'roll__student_name',
                                                                                        'roll__father_name',
                                                                                        'attendance',
                                                                                        'date_of_attendance', ).order_by(
                'roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=FirstYearattendance.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Attendance_Status', 'Date'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['attendance'],
                                 cdr['date_of_attendance']])
            return response
        elif data == 'Secondyear':
            newdata = Student_attendance.objects.filter(roll__student_detail__clas=data,
                                                        date_of_attendance=date).values('roll', 'roll__student_name',
                                                                                        'roll__father_name',
                                                                                        'attendance',
                                                                                        'date_of_attendance', ).order_by(
                'roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=SecondYearattendance.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Attendance_Status', 'Date'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['attendance'],
                                 cdr['date_of_attendance']])
            return response
        elif data == 'Ba':
            newdata = Student_attendance.objects.filter(roll__student_detail__clas=data,
                                                        date_of_attendance=date).values('roll', 'roll__student_name',
                                                                                        'roll__father_name',
                                                                                        'attendance',
                                                                                        'date_of_attendance', ).order_by(
                'roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Baattendance.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Attendance_Status', 'Date'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['attendance'],
                                 cdr['date_of_attendance']])
            return response
        elif data == 'Bsc':
            newdata = Student_attendance.objects.filter(roll__student_detail__clas=data,
                                                        date_of_attendance=date).values('roll', 'roll__student_name',
                                                                                        'roll__father_name',
                                                                                        'attendance',
                                                                                        'date_of_attendance', ).order_by(
                'roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Bscattendance.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Attendance_Status', 'Date'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['attendance'],
                                 cdr['date_of_attendance']])
            return response
        else:
            newdata = Student_attendance.objects.filter(roll__student_detail__clas=data,
                                                        date_of_attendance=date).values('roll', 'roll__student_name',
                                                                                        'roll__father_name',
                                                                                        'attendance',
                                                                                        'date_of_attendance', ).order_by(
                'roll')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=Bcomattendance.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Student_name', 'Father_name', 'Attendance_Status', 'Date'])
            for cdr in newdata:
                writer.writerow([cdr['roll'], cdr['roll__student_name'], cdr['roll__father_name'], cdr['attendance'],
                                 cdr['date_of_attendance']])
            return response
    else:
        return redirect('logedin')
def takeattendance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            droll = request.POST['roll']
            pattern = re.compile('^[0-9]{4,5}$')
            if pattern.match(droll):
                data = Student_attendance.objects.filter(roll=droll)
                if data:
                    Student_attendance.objects.filter(roll=droll,date_of_attendance=datetime.now()).update(attendance='Present')
                    messages.error(request, 'Done Succesfully')
                    return redirect('attendance:takeattendance')
                else:
                    messages.error(request, 'Invalid Roll Number')
                    return redirect('attendance:takeattendance')
            else:
                messages.error(request, 'Invalid Roll Number')
                return redirect('attendance:takeattendance')
        else:
            return render(request,'attendance.html')
    else:
        return redirect('logedin')