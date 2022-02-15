from django import forms
from .models import *

class teacher_info(forms.ModelForm):
    class Meta:
        model = Teacher_Info
        fields = ['teacher_name','teacher_fname','teacher_phone','teacher_cnic','teacher_addres','pay']
        widgets = {
            'teacher_name': forms.TextInput(attrs={'type': 'text', 'id': 'name-field', 'placeholder': 'Enter name', 'name': 'name','class': 'form-control', 'required': 'True'}),
            'teacher_fname': forms.TextInput(attrs={'type': 'text', 'id': 'fathername-field', 'placeholder': 'Enter father name','fathername': 'name', 'class': 'form-control', 'required': 'True'}),
            'teacher_phone': forms.TextInput(attrs={'type': 'tel', 'id': 'phone-field', 'placeholder': 'Enter phone number', 'name': 'phonenumber','class': 'form-control', 'required': 'True'}),
            'teacher_cnic': forms.TextInput(attrs={'type': 'text', 'id': 'cnic-field', 'placeholder': 'Enter CNIC', 'name': 'cnic','class': 'form-control', 'required': 'True'}),
            'teacher_addres': forms.TextInput(attrs={'type': 'text', 'id': 'addres-field', 'placeholder': 'Enter address', 'name': 'addres','class': 'form-control', 'required': 'True'}),
            'pay': forms.NumberInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter pay'}),
        }


""" class teacher_clas(forms.ModelForm):
    class Meta:
        model = Tea_class
        fields = ['clas']
        widgets = {
            'clas': forms.SelectMultiple(choices=Tea_class.objects.all(), attrs={'name': 'clas','class':'validate[required] form-control'})
        } """


""" class teacher_subj(forms.ModelForm):
    class Meta:
        model = Tea_subj
        fields = ['subjects']
        widgets={
            'subjects' : forms.SelectMultiple(choices=Tea_subj.objects.all(),attrs={'name':'subjects','class':'validate[required] form-control'})
        } """