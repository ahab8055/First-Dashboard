from django.db import models
from django.utils import timezone
from django.core.validators import *
from datetime import datetime
from django.contrib.auth import *
from django.contrib.auth.models import User
#Create your models here.
class Student_info(models.Model):
    roll = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=30,validators=[MinLengthValidator(3)])
    father_name = models.CharField(max_length=30,validators=[MinLengthValidator(3)])
    phone = models.CharField(max_length=12,validators=[MinLengthValidator(11)])
    addres = models.TextField(validators=[MinLengthValidator(15)])
    def __str__(self):
        return self.student_name


class Student_detail(models.Model):
    choice = [('Middel', 'Middel'), ('Nineth', '9th'), ('Tenth', '10th'), ('First year', '1st year'),
              ('Second year', '2nd year'), ('Bachelors', 'B.A'), ('Bsc', 'Bsc'), ('Bcom', 'Bcom')]
    roll = models.ForeignKey(Student_info,on_delete=models.CASCADE)
    clas = models.CharField(max_length=30, choices=choice)
    clas_fee = models.IntegerField(validators=[MinValueValidator(1000)])
    subject = models.CharField(max_length=10)
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.roll
