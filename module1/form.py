from django import forms
from django.contrib.auth.hashers import check_password
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
class loginform(forms.Form):
        name = forms.CharField(widget=forms.TextInput(attrs={'id':'uname','placeholder':'Enter name','name':'uname','class':'form-control'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','id':'password-field','placeholder':'Enter password','name':'password','class':'form-control'}))


""" class studentinfo(forms.ModelForm):
    class Meta:
        model = studentinfo
        fields = ['student_name','father_name','phone','addres']
        widgets = {
                    'student_name':forms.TextInput(attrs={'type':'text','id':'name-field','placeholder':'Enter name','name':'name','class':'form-control','required':'True'}),
                    'father_name': forms.TextInput(attrs={'type':'text','id':'fathername-field','placeholder':'Enter father name','fathername':'name','class':'form-control','required':'True'}),
                    'phone':forms.TextInput(attrs={'type':'tel','id':'phone-field','placeholder':'Enter phone number','name':'phonenumber','class':'form-control','required':'True'}),
                    'addres':forms.TextInput(attrs={'type':'text','id':'addres-field','placeholder':'Enter address','name':'addres','class':'form-control','required':'True'}),
                    } """

""" class student_detail(forms.ModelForm):
    class Meta:
        model=Student_detail
        fields=['clas_fee','clas']
        widgets={
            'clas': forms.Select(choices=Student_detail.objects.all(),attrs={'class': 'validate[required] form-control', 'id': 'clas-field',"onChange": 'Populate("clas-field","subjects-field")'}),
            'clas_fee': forms.NumberInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter fee'}),
        } """

class adminuser(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter name', 'name': 'username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password-field', 'placeholder': 'Enter password', 'name': 'password', 'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'confirmpassword-field', 'placeholder': 'Confirm password', 'name': 'confirm_password', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email-field', 'placeholder': 'Enter email', 'name': 'email', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','email','password')

    def clean(self):
        cleaned_data = super(adminuser, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

    def save(self, commit=True):
        user = super(adminuser, self).save(commit)
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user