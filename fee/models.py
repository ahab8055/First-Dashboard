from django.db import models
from datetime import *
from module1.models import *
# Create your models here.


class Fee_detail(models.Model):
    dat = str(datetime.now().month) + '-' + str(datetime.now().year)
    roll = models.ForeignKey(Student_info,on_delete=models.CASCADE)
    fee_status = models.CharField(max_length=10, default='Pending')
    month = models.CharField(max_length=10, default=dat)
    def __str__(self):
        return self.roll
