from django import forms
from .models import *
class attendancedate(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date','name':'date','class':'input-group date form-control'}))
class attendance_detail(forms.ModelForm):
    class Meta:
        # model = Student_attendance
        fields = ['attendance','date_of_attendance']
        widgets={
            'date_of_attendance':forms.DateInput(attrs={'class':'validate[required] form-control','disabled':'True'}),
            'attendance':forms.Select(attrs={'class':'validate[required] form-control','name':'attendance'},choices=[('Present','Present'),('Absent','Absent')])
        }