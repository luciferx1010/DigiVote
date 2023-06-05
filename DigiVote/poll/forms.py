from django import forms
#from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.admin.widgets import AdminDateWidget

year=[int(i) for i in range(1930,2050)]

class CustomUserCreationForm(UserCreationForm):
    #'aadharnumber','Mobilenumber','username', 'email','first_name', 'last_name', 'password'
    #aadharnumber,Mobilenumber,username,first_name,last_name,email,password
    class Meta:
        model = CustomUser
        fields = ['aadharnumber','Mobilenumber','username','first_name','last_name','email','dob']
        widgets = {
            'password': forms.PasswordInput,
            'dob' : forms.SelectDateWidget(years=year),
        }
        
class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ['Mobilenumber','username', 'email','first_name', 'last_name']


'''
class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    aadharnumber=forms.CharField(max_length=12)
    Mobilenumber=forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ['aadharnumber','Mobilenumber','username', 'first_name', 'last_name', 'email','password']
        widgets = {
            'password': forms.PasswordInput,
        }



class ChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
'''