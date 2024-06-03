from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
# Register your models here.

class ProfileAdmin(UserAdmin):
    pass
admin.site.register(UserProfile, ProfileAdmin)