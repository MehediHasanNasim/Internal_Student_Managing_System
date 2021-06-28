from django.shortcuts import render, redirect, HttpResponseRedirect
from itsapp import forms
from .models import Student
from .forms import StudentForm, ProfilePictureForm, UserCreationForm, StudentFormtwo
# Create your views here.

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

#import for login and signup
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# for email verification
import uuid 
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    diction= {}
    return render(request, 'itsapp/home.html', context=diction) 

def admin_homepage(request):
    student_list = Student.objects.order_by('first_name')
    diction= {'student_list':student_list} 
    return render(request, 'itsapp/admin_home.html', context=diction) 



def student_form(request):
    form = forms.StudentForm()

    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES)
    
        if form.is_valid():
            form.save(commit=True)
            return admin_homepage(request)

    diction = {"student_form":form}
    return render(request, 'itsapp/student_form.html', context=diction)


def about_us(request):
    diction= {}
    return render(request, 'itsapp/about_us.html', context=diction) 

def location(request):
    diction= {}
    return render(request, 'itsapp/location.html', context=diction) 

def notice(request):
    diction= {}
    return render(request, 'itsapp/notice.html', context=diction) 

def student_info(request, id):
    student = Student.objects.filter(pk=id)
    if student:
        student= Student.objects.get(pk=id)
    diction = {'student':student}
    return render (request, 'itsapp/student_info.html', context=diction)



def student_update(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    form = forms.StudentForm(instance=student_info)

    if request.method =="POST":
        form = forms.StudentForm(request.POST, instance=student_info)
        
        if form.is_valid():
            form.save(commit=True)
            return admin_homepage(request)

    diction = {'student_form': form}
    return render (request, 'itsapp/student_update.html', context=diction)


def student_delete(request, student_id):
    student= Student.objects.get(pk=student_id).delete()
    diction = {'delete_message': "Delete Done"}
    return render (request, 'itsapp/student_delete.html', context=diction)

def loginpage(request):

    if(request.user.is_authenticated):
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            #for email verification
            myform = User.objects.filter(username = username).first()
            if  myform is None:
                return redirect('/login')

            student_obj = Student.objects.filter(user = myform).first()

            if not student_obj.is_verified:
                messages.success(request, 'Profile is not verified, check your mail' )
                return redirect('/login') 


            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                messages.info(request, 'Incorrect Username or Password')

        diction = {}
        return render(request, 'itsapp/userlogin.html', context=diction)


@login_required(login_url='loginpage')
def userprofile(request):
    diction= {}
    return render(request, 'itsapp/userprofile.html', context=diction) 


def registerpage(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else:
        myform = UserCreationForm()
        if request.method == 'POST':
            
            myform = UserCreationForm(request.POST)
            username= request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if myform.is_valid():
                myform.save(commit=True)
                username = User.objects.get(username=username)

                auth_token = str(uuid.uuid4())
                print(username)
                
                student_obj = Student(user = username, auth_token = auth_token)
                student_obj.save()
                
                send_email_after_registration(email,auth_token)
                return redirect('/token')
                

        diction = {'myform':myform}
        return render(request, 'itsapp/usersignup.html', context=diction)
    


def notfound(request):
    diction = {}
    return render(request, 'itsapp/notfound.html', context=diction)

@login_required(login_url='loginpage')
def logoutuser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='loginpage')
def delete_my_account(request):
    if request.method=="POST":
        userdata = request.user.id
        delete_id =  User.objects.get(id=userdata)
        delete_id.delete()
        logout(request)
        return redirect('home')


#email verification items 
def success(request):
    return render(request, 'itsapp/success.html')

def token_send(request):
    return render(request, 'itsapp/token_send.html')


def verify(request, auth_token):
    try:
        student_obj= Student.objects.filter(auth_token = auth_token).first()
        if student_obj:
            if student_obj.is_verified:
                messages.success(request, 'Your Profile is already verified.')
                return redirect('loginpage') 
            student_obj.is_verified = True
            student_obj.save()
            messages.success(request, 'Your Account has been verified.')
            return redirect('loginpage')
        else:
            return redirect('/error')

    except Exception as e:
        print(e)  
        return redirect('home') 

def error(request):
    return render(request, 'itsapp/error.html')

def send_email_after_registration(email, token):
    
    subject = 'Your account needs to verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)



