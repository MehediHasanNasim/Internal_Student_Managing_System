from django.contrib import admin
from django.urls import path
from itsapp import views



urlpatterns = [
    path('', views.home, name='home'),
    path('admin_home/', views.admin_homepage, name="admin_home"),
    path('student_form/', views.student_form, name="student_form"),
    path('about/', views.about_us, name="about_us"),
    path('location/', views.location, name="location"),
    path('notice/', views.notice, name="notice"),
    path('student/<int:id>/', views.student_info, name="student_info"),
    path('student_update/<int:student_id>/', views.student_update, name="student_update"),
    path('student_delete/<int:student_id>/', views.student_delete, name="student_delete"),
    path('login/', views.loginpage, name="loginpage"),
    path('user/', views.userprofile, name="userprofile"),
    path('signup/', views.registerpage, name="registerpage"),
    path('notfound/', views.notfound, name="notfound"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('delete_my_account/', views.delete_my_account, name="delete_my_account"),
    path('success/', views.success, name="success"),
    path('token/', views.token_send, name="token_send"),
    path('verify/<auth_token>', views.verify, name='verify'),
    path('error/', views.error, name="error"),


]
