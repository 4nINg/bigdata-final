from django.contrib import admin
from django.db import models

from .models import Profile
# from django.contrib.auth.models import User
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nickname')

admin.site.register(Profile, ProfileAdmin)


