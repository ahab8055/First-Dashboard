from django.shortcuts import render,redirect
from django.db.models import Q
from teacher.form import *
import csv
from django.db.models import Sum
from django.http import HttpResponse
from .form import *
from  django.contrib import messages
from django.contrib.auth.models import *
from datetime import *
from fee.form import *
from attendance.form import *
from attendance.models import Student_attendance
from django.core.mail import EmailMessage
# Create your views here.
count = 0
def adminregistration(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = adminuser(request.POST)
            if form.is_valid():
                if User.objects.filter(email=form.cleaned_data['email']):
                    return redirect('adminregistration')
                else:
                    name = form.cleaned_data['username']
                    pas = form.cleaned_data['password']
                    email = form.cleaned_data['email']
                    u = User.objects.create_user(username=name,password=pas,email=email)
                    u.set_password(pas)
                    return redirect('index')
            else:
                messages.error(request, 'Invalid Info')
                return redirect('adminregistration')
        else:
            form = adminuser()
            return render(request,'adminregistration.html',{'form':form})
    else:
        return redirect('logedin')
def studentregistration(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_studentinfo = studentinfo(request.POST)
            form_student_detail = student_detail(request.POST)
            form_fee_detail = fee_detail()
            subject = request.POST['subject']
            if form_studentinfo.is_valid() and form_student_detail.is_valid():
                clas = form_student_detail.cleaned_data['clas']
                name = form_studentinfo.cleaned_data['student_name']
                fathername = form_studentinfo.cleaned_data['father_name']
                resultname = Student_detail.objects.filter(clas=clas).order_by('roll_id')
                if resultname :
                    data = Student_detail.objects.filter(roll__student_name__exact=name,roll__father_name__exact=fathername,clas=clas)
                    if data :
                        messages.error(request, 'Student already exist')
                        return redirect('studentregisteration')
                    else:
                        result = Student_detail.objects.filter(clas=clas).earliest('roll')
                        for n in resultname:
                            if n.roll_id == result.roll_id:
                                result.roll_id = result.roll_id + 1
                            else:
                                break
                        inc = result.roll_id
                        usr = form_studentinfo.save(commit=False)
                        usr.roll = inc
                        usr.save()
                        usr1 = form_student_detail.save(commit=False)
                        usr1.roll = usr
                        usr1.subject = subject
                        usr1.save()
                        obj2 = form_fee_detail.save(commit=False)
                        obj2.roll = usr
                        obj2.save()
                        Student_attendance.objects.get_or_create(roll_id=usr.roll, attendance='Absent',date_of_attendance=datetime.now())
                        return redirect('index')
                else:
                    if clas == 'Middel':
                        obj = form_studentinfo.save(commit=False)
                        obj.roll = 8000
                        obj.save()
                        obj1 = form_student_detail.save(commit=False)
                        obj1.roll = obj
                        obj1.subject=subject
                        obj1.save()
                        obj2 = form_fee_detail.save(commit=False)
                        obj2.roll = obj
                        obj2.save()
                        Student_attendance.objects.get_or_create(roll_id=obj.roll, attendance='Absent',date_of_attendance=datetime.now())
                        return redirect('index')
                    elif clas == 'Nineth':
                        obj = form_studentinfo.save(commit=False)
                        obj.roll = 9000
                        obj.save()
                        obj1 = form_student_detail.save(commit=False)
                        obj1.roll = obj
                        obj1.subject = subject
                        obj1.save()
                        obj2 = form_fee_detail.save(commit=False)
                        obj2.roll = obj
                        obj2.save()
                        Student_attendance.objects.get_or_create(roll_id=obj.roll, attendance='Absent',
                                                                 date_of_attendance=datetime.now())
                        return redirect('index')
                    elif clas == 'Tenth':
                        obj = form_studentinfo.save(commit=False)
                        obj.roll = 10000
                        obj.save()
                        obj1 = form_student_detail.save(commit=False)
                        obj1.roll = obj
                        obj1.subject = subject
                        obj1.save()
                        obj2 = form_fee_detail.save(commit=False)
                        obj2.roll = obj
                        obj2.save()
                        Student_attendance.objects.get_or_create(roll_id=obj.roll, attendance='Absent',
                                                                 date_of_attendance=datetime.now())
                        return redirect('index')
                    elif clas == 'First year':
                        obj = form_studentinfo.save(commit=False)
                        obj.roll = 11000
                        obj.save()
                        obj1 = form_student_detail.save(commit=False)
                        obj1.roll = obj
                        obj1.subject = subject
                        obj1.save()
                        obj2 = form_fee_detail.save(commit=False)
                        obj2.roll = obj
                        obj2.save()
                        Student_attendance.objects.get_or_create(roll_id=obj.roll, attendance='Absent',
                                                                 date_of_attendance=datetime.now())
                        return redirect('index')
                    elif clas == 'Second year':
                        obj = form_studentinfo.save(commit=False)
                        obj.roll = 12000
                        obj.save()
                        obj1 = form_student_detail.save(commit=False)
                        obj1.roll = obj
                        obj1.subject = subject
                        obj1.save()
                        obj2 = form_fee_detail.save(commit=False)
                        obj2.roll = obj
                        obj2.save()
                        Student_attendance.objects.get_or_create(roll_id=obj.roll, attendance='Absent',
                                                                 date_of_attendance=datetime.now())
                        return redirect('index')
                    elif clas == 'Bachelors':
                        obj = form_studentinfo.save(commit=False)
                        obj.roll = 13000
                        obj.save()
                        obj1 = form_student_detail.save(commit=False)
                        obj1.roll = obj
                        obj1.subject = subject
                        obj1.save()
                        obj2 = form_fee_detail.save(commit=False)
                        obj2.roll = obj
                        obj2.save()
                        Student_attendance.objects.get_or_create(roll_id=obj.roll, attendance='Absent',
                                                                 date_of_attendance=datetime.now())
                        return redirect('index')
                    elif clas == 'Bsc':
                        obj = form_studentinfo.save(commit=False)
                        obj.roll = 14000
                        obj.save()
                        obj1 = form_student_detail.save(commit=False)
                        obj1.roll = obj
                        obj1.subject = subject
                        obj1.save()
                        obj2 = form_fee_detail.save(commit=False)
                        obj2.roll = obj
                        obj2.save()
                        Student_attendance.objects.get_or_create(roll_id=obj.roll, attendance='Absent',
                                                                 date_of_attendance=datetime.now())
                        return redirect('index')
                    else:
                        obj = form_studentinfo.save(commit=False)
                        obj.roll = 15000
                        obj.save()
                        obj1 = form_student_detail.save(commit=False)
                        obj1.roll = obj
                        obj1.subject = subject
                        obj1.save()
                        obj2 = form_fee_detail.save(commit=False)
                        obj2.roll = obj
                        obj2.save()
                        Student_attendance.objects.get_or_create(roll_id=obj.roll, attendance='Absent',
                                                                 date_of_attendance=datetime.now())
                        return redirect('index')
            else:
                messages.error(request, 'Invalid Data')
                return redirect('studentregisteration')
        else:
            # form_studentinfo = studentinfo()
            form_studentinfo = 'form_studentinfo'
            # form_student_detail = student_detail()
            form_student_detail = 'student_detail'
            return render(request, 'studentregistration.html', {'form_studentinfo': form_studentinfo,'form_student_detail':form_student_detail})
    else:
        return redirect('logedin')
def teacherregistration(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_tea_info = teacher_info(request.POST)
            form_tea_clas = teacher_clas(request.POST)
            form_tea_subj = teacher_subj(request.POST)
            if form_tea_info.is_valid():
                dat = form_tea_info.cleaned_data['teacher_cnic']
                info = Teacher_Info.objects.filter(teacher_cnic__exact=dat)
                if info:
                    messages.error(request, 'Teacher already exist')
                    return redirect('teacherregistration')
                else:
                    data_clas = request.POST.getlist('clas')
                    data_subj = request.POST.getlist('subjects')
                    if '' in data_clas or '' in data_subj:
                        messages.error(request, 'Invalid Data')
                        return redirect('teacherregistration')
                    else:
                        len_clas = len(data_clas)
                        len_subj = len(data_subj)
                        obj = form_tea_info.save()
                        data = ''
                        for i in range(0,len_clas):
                            if i == 0:
                                data = data_clas[i]
                            if i > 0 :
                                data = data + ',' + data_clas[i]
                            if i == len_clas - 1 :
                                Tea_class.objects.create(t_id=obj,clas=data)
                        for i in range(0, len_subj):
                            if i == 0:
                                data = data_subj[i]
                            if i > 0:
                                data = data + ',' + data_subj[i]
                            if i == len_subj - 1:
                                Tea_subj.objects.create(t_id=obj, subjects=data)
                        return redirect('index')
            else:
                return render(request,'teacherregistration.html',{'form':form_tea_info})
        else:
            form_tea_info = teacher_info()
            form_tea_clas = teacher_clas()
            form_tea_subj = teacher_subj()
            return render(request,'teacherregistration.html',{'form_tea_info':form_tea_info,'form_tea_clas':form_tea_clas,'form_tea_subj':form_tea_subj})
    else:
        return redirect('logedin')
def search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data_st = ''
            data_te = ''
            data_post = request.POST['search']
            if studentinfo.objects.filter(Q(student_name__icontains=data_post) | Q(father_name__icontains=data_post) | Q(phone=data_post)) or Teacher_Info.objects.filter(Q(teacher_name__icontains=data_post) | Q(teacher_fname__icontains=data_post) | Q(teacher_phone=data_post)):
                if studentinfo.objects.filter(Q(student_name__icontains=data_post) | Q(father_name__icontains=data_post) | Q(phone=data_post)):
                    data_st = studentinfo.objects.filter(Q(student_name__icontains=data_post) | Q(father_name__icontains=data_post) | Q(phone=data_post)).values('roll','student_name','father_name','phone','student_detail__clas')
                if Teacher_Info.objects.filter(Q(teacher_name__icontains=data_post) | Q(teacher_fname__icontains=data_post) | Q(teacher_phone=data_post)):
                    data_te = Teacher_Info.objects.filter(Q(teacher_name__icontains=data_post) | Q(teacher_fname__icontains=data_post) | Q(teacher_phone=data_post)).values('teacher_name','teacher_fname','teacher_phone','teacher_cnic')
                return render(request,'data.html',{'data_st':data_st,'data_te':data_te})
            elif Teacher_Info.objects.filter(teacher_cnic=data_post):
                data_te = Teacher_Info.objects.filter(teacher_cnic=data_post).values('teacher_name','teacher_fname','teacher_phone','teacher_cnic')
                return render(request,'data.html',{'data_te':data_te})
            else:
                try:
                    data_st = studentinfo.objects.filter(roll=data_post).values('roll','student_name','father_name','phone','student_detail__clas')
                    return render(request,'data.html',{'data_st':data_st})
                except:
                    return render(request,'data.html')
        else:
            return redirect('index')
    else:
        return redirect('logedin')
def index(request):
    if request.user.is_authenticated:
        dat = str(datetime.now().month) + '-' + str(datetime.now().year)
        # tpresents = Student_attendance.objects.filter(attendance='Present',date_of_attendance=datetime.now()).count()
        tpresents = 50
        # tabsents = Student_attendance.objects.filter(attendance='Absent', date_of_attendance=datetime.now()).count()
        tabsents = 50
        # tpaid = Student_detail.objects.filter(roll__fee_detail__fee_status='Paid',roll__fee_detail__month=dat).aggregate(Sum('clas_fee'))
        # tpending = Student_detail.objects.filter(roll__fee_detail__fee_status='Pending',roll__fee_detail__month=dat).aggregate(Sum('clas_fee'))
        # teacherpay = Teacher_Info.objects.all().aggregate(Sum('pay'))
        teacherpay = { 'pay__sum': None }
        # totalstudents =  studentinfo.objects.all().count()
        totalstudents =  100
        tpending = 'tpending'
        tpaid = 'tpaid'
        fpaid =  2000
        fpending =  150
        if teacherpay['pay__sum'] == None:
            tpay = 10
        else:
            tpay = int(teacherpay['pay__sum'])
        """ if tpaid['clas_fee__sum'] == None:
            fpaid = 0
        else:
            fpaid = int(tpaid['clas_fee__sum'])
        if tpending['clas_fee__sum'] == None:
            fpending = 0
        else:
            fpending = int(tpending['clas_fee__sum']) """
        percentst = int((tpresents/totalstudents)*100)
        totalfee = fpaid + fpending
        percentfee = int((fpaid / totalfee) * 100)
        profit = int(((fpaid - tpay)/tpay)*100)
        return render(request,'index.html',{'tpresents':tpresents,'tabsents':tabsents,'tpaid':tpaid,'tpending':tpending,'percentst':percentst,'percentfee':percentfee,'profit':profit})
    else:
        return redirect('logedin')
def logedout(request):
    logout(request)
    return redirect('logedin')
def logedin(request):
    chk1 = 0
    chk2 = 0
    global count
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pas = form.cleaned_data['password']
            user=authenticate(username=name,password=pas)
            if user is not None:
                #sendemail(request)
                count = 0
                login(request,user)
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])
                return redirect('index')
            else:
                count = count + 1
                try:
                    x = User.objects.get(username=name)
                except User.DoesNotExist:
                    chk1 = 1
                try:
                    x =User.objects.get(password=pas)
                except User.DoesNotExist:
                    chk2 = 1
                if chk1 == 1 and chk2 == 1:
                    messages.error(request, 'Invalid username and paswword !')
                elif chk1 == 1:
                    messages.error(request, 'Invalid username !')
                else:
                    messages.error(request, 'Invalid Password !')
                if count == 3:
                    count = 0
                    sendemail(request,name,pas)
                return redirect('logedin')
        else:
            return redirect('logedin')
    else:
        form = loginform()
        return render(request, 'login.html', {'form':form})
def sendemail(request,name,pas):
    reciver = []
    for useremail in User.objects.all():
        reciver.append(useremail.email)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    subject = 'To let u know about login'
    message = 'Someone is logedin into your account having ip addres ' + str(ip) + ' with credentials name ' + str(name) + ' and password ' + str(pas) + ' so please update your password '
    try:
        email = EmailMessage(subject, message, to=reciver)
        email.send()
    except Exception as e:
        return redirect('logedin')
def monthname(mon):
    if mon == '1-':
        month = 'January'
    elif mon == '2-':
        month = 'February'
    elif mon == '3-':
        month = 'March'
    elif mon == '4-':
        month = 'April'
    elif mon == '5-':
        month = 'May'
    elif mon == '6-':
        month = 'June'
    elif mon == '7-':
        month = 'July'
    elif mon == '8-':
        month = 'August'
    elif mon == '9-':
        month = 'September'
    elif mon == '10':
        month = 'October'
    elif mon == '11':
        month = 'November'
    else:
        month = 'December'
    return month
def detail(request,id):
    if request.user.is_authenticated:
        data_genral_detail = studentinfo.objects.filter(roll=id).values('roll','student_name','father_name','addres','phone','student_detail__clas','student_detail__clas_fee','student_detail__subject')
        data_attendance_detail = Student_attendance.objects.filter(roll=id).values('attendance','date_of_attendance').order_by('date_of_attendance')
        data_fee_detail = Fee_detail.objects.filter(roll=id).values('month','fee_status').order_by('month')
        return render(request,'detail_student.html',{'data_genral_detail':data_genral_detail,'data_attendance_detail':data_attendance_detail,'data_fee_detail':data_fee_detail,'roll':id})
    else:
        return redirect('logedin')
def edit(request,id,data):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if data == 'genral':
                data_studentinfo = studentinfo.objects.get(pk=id)
                data_student_detail = Student_detail.objects.get(roll=id)
                clas = data_student_detail.clas
                form_studentinfo = studentinfo(request.POST)
                form_student_detail = student_detail(request.POST)
                if form_studentinfo.is_valid() and form_student_detail.is_valid():
                    data_student_detail.subject = request.POST['subject']
                    if clas != request.POST['clas']:
                        resultname = Student_detail.objects.filter(clas=form_student_detail.cleaned_data['clas']).order_by('roll_id')
                        if resultname:
                            newdata = Student_detail.objects.filter(roll__student_name__exact=form_studentinfo.cleaned_data['student_name'],roll__father_name__exact=form_studentinfo.cleaned_data['father_name'], clas=form_student_detail.cleaned_data['clas']).exclude(pk=id)
                            if newdata:
                                messages.error(request, 'Student already exist')
                                return redirect('edit',id,data)
                            else:
                                result = Student_detail.objects.filter(
                                    clas=form_student_detail.cleaned_data['clas']).earliest('roll')
                                for n in resultname:
                                    if n.roll_id == result.roll_id:
                                        result.roll_id = result.roll_id + 1
                                    else:
                                        break
                                studentinfo.objects.filter(roll=id).update(roll=result.roll_id,
                                                                            student_name=form_studentinfo.cleaned_data[
                                                                                'student_name'],
                                                                            father_name=form_studentinfo.cleaned_data[
                                                                                'father_name'])
                                data_student_detail.roll_id = result.roll_id
                                data_student_detail.clas = form_student_detail.cleaned_data['clas']
                                data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                                data_student_detail.save()
                                Student_attendance.objects.filter(roll=id).update(roll=result.roll_id)
                                Fee_detail.objects.filter(roll=id).update(roll=result.roll_id)
                                return redirect('index')
                        else:
                            if form_student_detail.cleaned_data['clas'] == 'Middel':
                                studentinfo.objects.filter(roll=id).update(roll=8000,student_name=form_studentinfo.cleaned_data['student_name'],father_name=form_studentinfo.cleaned_data['father_name'])
                                data_student_detail.roll_id = 8000
                                data_student_detail.clas = form_student_detail.cleaned_data['clas']
                                data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                                data_student_detail.save()
                                Student_attendance.objects.filter(roll=id).update(roll=8000)
                                Fee_detail.objects.filter(roll=id).update(roll=8000)
                                return redirect('index')
                            elif form_student_detail.cleaned_data['clas'] == 'Nineth':
                                studentinfo.objects.filter(roll=id).update(roll=9000,
                                                                            student_name=form_studentinfo.cleaned_data[
                                                                                'student_name'],
                                                                            father_name=form_studentinfo.cleaned_data[
                                                                                'father_name'])
                                data_student_detail.roll_id = 9000
                                data_student_detail.clas = form_student_detail.cleaned_data['clas']
                                data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                                data_student_detail.save()
                                Student_attendance.objects.filter(roll=id).update(roll=9000)
                                Fee_detail.objects.filter(roll=id).update(roll=9000)
                                return redirect('index')
                            elif form_student_detail.cleaned_data['clas'] == 'Tenth':
                                studentinfo.objects.filter(roll=id).update(roll=10000,
                                                                            student_name=form_studentinfo.cleaned_data[
                                                                                'student_name'],
                                                                            father_name=form_studentinfo.cleaned_data[
                                                                                'father_name'])
                                data_student_detail.roll_id = 10000
                                data_student_detail.clas = form_student_detail.cleaned_data['clas']
                                data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                                data_student_detail.save()
                                Student_attendance.objects.filter(roll=id).update(roll=10000)
                                Fee_detail.objects.filter(roll=id).update(roll=10000)
                                return redirect('index')
                            elif form_student_detail.cleaned_data['clas'] == 'First year':
                                studentinfo.objects.filter(roll=id).update(roll=11000,
                                                                            student_name=form_studentinfo.cleaned_data[
                                                                                'student_name'],
                                                                            father_name=form_studentinfo.cleaned_data[
                                                                                'father_name'])
                                data_student_detail.roll_id = 11000
                                data_student_detail.clas = form_student_detail.cleaned_data['clas']
                                data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                                data_student_detail.save()
                                Student_attendance.objects.filter(roll=id).update(roll=11000)
                                Fee_detail.objects.filter(roll=id).update(roll=11000)
                                return redirect('index')
                            elif form_student_detail.cleaned_data['clas'] == 'Second year':
                                studentinfo.objects.filter(roll=id).update(roll=12000,
                                                                            student_name=form_studentinfo.cleaned_data[
                                                                                'student_name'],
                                                                            father_name=form_studentinfo.cleaned_data[
                                                                                'father_name'])
                                data_student_detail.roll_id = 12000
                                data_student_detail.clas = form_student_detail.cleaned_data['clas']
                                data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                                data_student_detail.save()
                                Student_attendance.objects.filter(roll=id).update(roll=12000)
                                Fee_detail.objects.filter(roll=id).update(roll=12000)
                                return redirect('index')
                            elif form_student_detail.cleaned_data['clas'] == 'Bachelors':
                                studentinfo.objects.filter(roll=id).update(roll=13000,
                                                                            student_name=form_studentinfo.cleaned_data[
                                                                                'student_name'],
                                                                            father_name=form_studentinfo.cleaned_data[
                                                                                'father_name'])
                                data_student_detail.roll_id = 13000
                                data_student_detail.clas = form_student_detail.cleaned_data['clas']
                                data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                                data_student_detail.save()
                                Student_attendance.objects.filter(roll=id).update(roll=13000)
                                Fee_detail.objects.filter(roll=id).update(roll=13000)
                                return redirect('index')
                            elif form_student_detail.cleaned_data['clas'] == 'Bsc':
                                studentinfo.objects.filter(roll=id).update(roll=14000,
                                                                            student_name=form_studentinfo.cleaned_data[
                                                                                'student_name'],
                                                                            father_name=form_studentinfo.cleaned_data[
                                                                                'father_name'])
                                data_student_detail.roll_id = 14000
                                data_student_detail.clas = form_student_detail.cleaned_data['clas']
                                data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                                data_student_detail.save()
                                Student_attendance.objects.filter(roll=id).update(roll=14000)
                                Fee_detail.objects.filter(roll=id).update(roll=14000)
                                return redirect('index')
                            else:
                                studentinfo.objects.filter(roll=id).update(roll=15000,
                                                                            student_name=form_studentinfo.cleaned_data[
                                                                                'student_name'],
                                                                            father_name=form_studentinfo.cleaned_data[
                                                                                'father_name'])
                                data_student_detail.roll_id = 15000
                                data_student_detail.clas = form_student_detail.cleaned_data['clas']
                                data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                                data_student_detail.save()
                                Student_attendance.objects.filter(roll=id).update(roll=15000)
                                Fee_detail.objects.filter(roll=id).update(roll=15000)
                                return redirect('index')
                    else:
                        newdata = Student_detail.objects.filter(
                            roll__student_name__exact=form_studentinfo.cleaned_data['student_name'],
                            roll__father_name__exact=form_studentinfo.cleaned_data['father_name'],
                            clas=form_student_detail.cleaned_data['clas']).exclude(pk=id)
                        if newdata:
                            messages.error(request, 'Student already exist')
                            return redirect('edit',id,data)
                        else:
                            data_studentinfo.student_name = form_studentinfo.cleaned_data['student_name']
                            data_studentinfo.father_name = form_studentinfo.cleaned_data['father_name']
                            data_studentinfo.phone = form_studentinfo.cleaned_data['phone']
                            data_studentinfo.addres = form_studentinfo.cleaned_data['addres']
                            data_student_detail.clas = form_student_detail.cleaned_data['clas']
                            data_student_detail.clas_fee = form_student_detail.cleaned_data['clas_fee']
                            data_student_detail.save()
                            data_studentinfo.save()
                            return redirect('index')
                else:
                    return redirect('edit',id,data)
            elif data == 'attendance':
                count = 0
                form_attendance_detail = attendance_detail(request.POST)
                data_list = request.POST.getlist('attendance')
                data_attendance_detail = Student_attendance.objects.filter(roll=id).order_by('date_of_attendance')
                for info in data_attendance_detail:
                    info.attendance = data_list[count]
                    info.save()
                    count = count + 1
                return redirect('index')
            else:
                count = 0
                form_fee_detail = fee_detail(request.POST)
                data_list = request.POST.getlist('fee_status')
                data_fee_detail = Fee_detail.objects.filter(roll=id).order_by('month')
                for info in data_fee_detail:
                    info.fee_status = data_list[count]
                    info.save()
                    count = count + 1
                return redirect('index')
        else:
            if data == 'genral':
                data_studentinfo = studentinfo.objects.get(roll=id)
                data_student_detail = Student_detail.objects.get(roll=id)
                form_studentinfo = studentinfo(initial={'student_name':data_studentinfo.student_name,'father_name':data_studentinfo.father_name,'phone':data_studentinfo.phone,'addres':data_studentinfo.addres})
                form_student_detail = student_detail(initial={'clas':data_student_detail.clas,'clas_fee':data_student_detail.clas_fee,'subject':data_student_detail.subject})
                return render(request,'edit.html',{'roll':id,'form_studentinfo':form_studentinfo,'form_student_detail':form_student_detail,'data':data})
            elif data == 'attendance':
                form_attendance_info = []
                data_attendance_info = Student_attendance.objects.filter(roll=id).order_by('date_of_attendance')
                for info in data_attendance_info:
                    form_attendance_info.append(attendance_detail(initial={'date_of_attendance': info.date_of_attendance, 'attendance': info.attendance}))
                return render(request, 'edit.html', {'roll': id, 'form_attendance_info': form_attendance_info, 'data': data})
            else:
                form_fee_info = []
                data_fee_info = Fee_detail.objects.filter(roll=id).order_by('month')
                for info in data_fee_info:
                    form_fee_info.append(fee_detail(initial={'month':info.month,'fee_status':info.fee_status}))
                return render(request, 'edit.html', {'roll': id, 'form_fee_info':form_fee_info, 'data': data})
    else:
     return  redirect('logedin')
def setting(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = User.objects.all()
            return render(request,'settings.html',{'data':data})
        else:
            data = User.objects.filter(is_superuser=0)
            return render(request, 'settings.html', {'data': data})
    else:
        redirect('logedin')
def admindetail(request,usr):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                info = User.objects.get(username=usr)
                form = adminuser(request.POST,instance=info)
                if form.is_valid():
                    if User.objects.filter(email=form.cleaned_data['email']).exclude(pk=info.id):
                        return redirect('admindetail',usr)
                    else:
                        form.save()
                        info.set_password(form.cleaned_data['password'])
                        info.save()
                        return redirect('index')
                else:
                    return redirect('admindetail',usr)
            else:
                info = User.objects.get(username=usr)
                chk = info.is_superuser
                data = adminuser(initial={'username': info.username, 'email': info.email})
                return render(request, 'admindetail.html', {'data': data,'usr':usr,'chk':chk})
        else:
            return redirect('index')
    else:
        return redirect('logedin')
def delete(request,id):
    if request.user.is_authenticated:
        studentinfo.objects.get(pk=id).delete()
        return redirect('index')
    else:
        return redirect('logedin')
def deleteadmin(request,usr):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            User.objects.filter(username=usr).delete()
            return redirect('index')
        else:
            return redirect('index')
    else:
        return redirect('logedin')
def csvgenration(request,id,data):
    if request.user.is_authenticated:
        if data == 'fee':
            newdata = Fee_detail.objects.filter(roll=id)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=fee.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Month', 'Fee Status'])
            for cdr in newdata:
                writer.writerow([cdr.roll_id, cdr.month, cdr.fee_status])
            return response
        else:
            newdata = Student_attendance.objects.filter(roll=id).order_by('date_of_attendance')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=attendance.csv'
            writer = csv.writer(response)
            writer.writerow(['Roll', 'Date of attendance', 'Attendance'])
            for cdr in newdata:
                writer.writerow([cdr.roll_id, cdr.date_of_attendance, cdr.attendance])
            return response
    else:
        return redirect('logedin')
def detailteacher(request,cnic):
    if request.user.is_authenticated:
        data = Teacher_Info.objects.filter(teacher_cnic=cnic).values('teacher_name','teacher_fname','teacher_cnic','teacher_phone','teacher_addres','doj','pay','tea_class__clas','tea_subj__subjects')
        return render(request,'detail_teacher.html',{'data':data,'cnic':cnic})
    else:
        return redirect('logedin')
def editteacher(request,cnic):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data_teacher_info = Teacher_Info.objects.get(teacher_cnic=cnic)
            data_teacher_clas = Tea_class.objects.get(t_id__teacher_cnic=cnic)
            data_teacher_subj = Tea_subj.objects.get(t_id__teacher_cnic=cnic)
            form_teacher_info = teacher_info(request.POST,instance=data_teacher_info)
            form_teacher_clas = teacher_clas(request.POST,instance=data_teacher_clas)
            form_teacher_subj = teacher_subj(request.POST,instance=data_teacher_subj)
            if form_teacher_info.is_valid():
                data_clas = request.POST.getlist('clas')
                data_subj = request.POST.getlist('subjects')
                if '' in data_clas or '' in data_subj:
                    messages.error(request, 'Invalid Data')
                    return redirect('editteacher',cnic)
                else:
                    form_teacher_info.save()
                    len_clas = len(data_clas)
                    len_subj = len(data_subj)
                    data = ''
                    for i in range(0, len_clas):
                        if i == 0:
                            data = data_clas[i]
                        if i > 0:
                            data = data + ',' + data_clas[i]
                        if i == len_clas - 1:
                            Tea_class.objects.filter(t_id__teacher_cnic=cnic).update(clas=data)
                    for i in range(0, len_subj):
                        if i == 0:
                            data = data_subj[i]
                        if i > 0:
                            data = data + ',' + data_subj[i]
                        if i == len_subj - 1:
                            Tea_subj.objects.filter(t_id__teacher_cnic=cnic).update(subjects=data)
                    return redirect('index')
            else:
                messages.error(request, 'Invalid Data')
                return redirect('editteacher',cnic)
        else:
            data_teacher_info = Teacher_Info.objects.get(teacher_cnic=cnic)
            data_teacher_clas = Tea_class.objects.get(t_id__teacher_cnic=cnic)
            data_teacher_subj = Tea_subj.objects.get(t_id__teacher_cnic=cnic)
            form_tea_info = teacher_info(initial={'teacher_name':data_teacher_info.teacher_name,'teacher_fname':data_teacher_info.teacher_fname,'teacher_phone':data_teacher_info.teacher_phone,'teacher_addres':data_teacher_info.teacher_addres,'teacher_cnic':data_teacher_info.teacher_cnic,'pay':data_teacher_info.pay})
            form_tea_clas = teacher_clas(initial={'clas':data_teacher_clas.clas})
            form_tea_subj = teacher_subj(initial={'subjects':data_teacher_subj.subjects})
            return render(request, 'teacheredit.html',{'form_tea_info': form_tea_info, 'form_tea_clas': form_tea_clas, 'form_tea_subj': form_tea_subj,'cnic':cnic})
    else:
        return redirect('logedin')
def deleteteacher(request,cnic):
    if request.user.is_authenticated:
        Teacher_Info.objects.get(teacher_cnic=cnic).delete()
        return redirect('index')
    else:
        return redirect('logedin')