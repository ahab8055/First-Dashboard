from django import forms
from .models import *
class fee_date(forms.Form):
    choice = [('1','January'),('2','February'),('3','March'),('4','April'),('5','May'),('6','June'),('7','July'),('8','August'),('9','September'),('10','October'),('11','November'),('12','December')]
    month = forms.ChoiceField(choices=choice,widget=forms.Select(attrs={'name':'month','class':'form-control'}))

class fee_year(forms.Form):
    choice = [('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025'),('2026','2026'),('2027','2027'),('2028','2028'),('2029','2029'),('2030','2030'),]
    year = forms.ChoiceField(choices=choice,widget=forms.Select(attrs={'name': 'year', 'class': 'form-control'}))

class fee_detail(forms.ModelForm):
     class Meta:
         model=Fee_detail
         fields=['fee_status','month']
         widgets={
             'month':forms.TextInput(attrs={'class':'validate[required] form-control','disabled':'True'}),
             'fee_status':forms.Select(attrs={'class':'validate[required] form-control','name':'fee'},choices=[('Paid','Paid'),('Pending','Pending')])
         }