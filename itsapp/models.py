from django.db import models
from django.db.models import Model 
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Student(models.Model):
    user =       models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified =models.BooleanField(default=False)
    create_at =  models.DateTimeField(auto_now_add=True)
    photo =      models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100, null=True, blank=True, default='',) 
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    dept =       models.CharField(max_length=50)
    session =    models.CharField(max_length=50)
    roll =       models.IntegerField(null=True)
    reg =        models.IntegerField(null=True)
    phone =      models.IntegerField(null=True)
    atd_percent= models.IntegerField(null=True)
    due =        models.CharField(max_length=100)



    def __str__(self):
        return str(self.pk)+ " " + self.first_name+ " " + self.last_name

class ProfilePicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to='uploaded_image/user')







