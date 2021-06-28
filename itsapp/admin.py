from django.contrib import admin
from .models import Student, ProfilePicture
# Register your models here.

admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('photo', 'first_name', 'auth_token', 'is_verified', 'create_at', 'last_name','dept', 'session', 'roll', 'reg', 'phone', 'atd_percent', 'due')

 

@admin.register(ProfilePicture)
class ProfilePictureAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')