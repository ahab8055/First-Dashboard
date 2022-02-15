from django.db import models
from module1.models import *

# Create your models here.
class Student_attendance(models.Model):
    roll = models.ForeignKey(Student_info,to_field='roll',on_delete=models.CASCADE)
    attendance = models.CharField(max_length=10,default='Absent')
    date_of_attendance = models.DateField(default=timezone.now)
    def __str__(self):
        return self.roll
