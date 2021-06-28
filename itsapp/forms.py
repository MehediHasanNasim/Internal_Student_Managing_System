from django import forms
from itsapp import models
#for auth and profilep picture
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfilePicture, Student
from django.core import validators
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        model = models.Student
        fields = ['user', 'photo', 'first_name', 'last_name','dept', 'session', 'roll', 'reg', 'phone', 'atd_percent', 'due']

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = ['image']
    
class StudentFormtwo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']