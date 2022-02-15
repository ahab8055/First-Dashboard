from django.db import models
from django.utils import timezone
from django.core.validators import *
from datetime import datetime


class Teacher_Info(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=30,validators=[MinLengthValidator(3)])
    teacher_fname = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    teacher_phone = models.CharField(max_length=12, validators=[MinLengthValidator(11)])
    teacher_cnic = models.CharField(max_length=15,validators=[MinLengthValidator(13)])
    teacher_addres = models.TextField(validators=[MinLengthValidator(15)])
    doj = models.DateField(default=datetime.now())
    pay=models.IntegerField(validators=[MinValueValidator(1000)])
    def __str__(self):
        return self.teacher_name
    class Meta:
        db_table='Teacher_Info'

class Tea_subj(models.Model):
    option = [('Science', 'Science'), ('Arts', 'Arts'), ('Bio', 'Bio'), ('Physics', 'Physics'),
              ('Chemistry', 'Chemistry'), ('Computer', 'Computer'), ('English', 'English'), ('Urdu', 'Urdu'),
              ('Islamiyat', 'Islamiyat'), ('Pakstudies', 'Pak studies'), ('Stat', 'Stat'), ('Economics', 'Economics'),
              ('Accounting', 'Accounting'), ('Commerce', 'Commerce'), ('Banking', 'Banking')]
    t_id = models.ForeignKey(Teacher_Info,on_delete=models.CASCADE)
    subjects = models.CharField(max_length=50,choices=option)
    def __str__(self):
        return self.subjects
    class Meta:
        db_table='Teacher_subjects'

class Tea_class(models.Model):
    choice = [('Middel', 'Middel'), ('Nineth', '9th'), ('Tenth', '10th'), ('First year', '1st year'),
              ('Second year', '2nd year'), ('Bachelors', 'B.A'), ('Bsc', 'Bsc'), ('Bcom', 'Bcom')]
    t_id = models.ForeignKey(Teacher_Info,on_delete=models.CASCADE)
    clas = models.CharField(max_length=50,choices=choice)
    def __str__(self):
        return self.clas
    class Meta:
        db_table='Teacher_class'