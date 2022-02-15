from django.http import HttpResponse
from fee.models import *
from attendance.models import *
from datetime import *
def attendance():
    info = Student_info.objects.all().order_by('roll')
    data = Student_attendance.objects.filter(date_of_attendance__day=datetime.now().day)
    if data:
        pass
    else:
        for n in info:
            Student_attendance.objects.create(roll=n,attendance='Absent',date_of_attendance=datetime.now())
def fee():
    if datetime.now().day > 29:
        info = Student_info.objects.all().order_by('roll')
        dat = str(datetime.now().month)
        year = int(datetime.now().year)
        if dat == '12':
            dat = '1'
            year = year + 1
            dat = dat + '-' + str(year)
        else:
            dat = int(dat) + 1
            dat = str(dat) + '-' + str(year)
        for i in info :
                Fee_detail.objects.get_or_create(roll_id=i.roll,fee_status='Pending',month=dat)