from django.contrib import admin
from .models import Profile, Function, Ingredient, Product
# from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Profile)
admin.site.register(Function)
admin.site.register(Ingredient)
admin.site.register(Product)
