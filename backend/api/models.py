from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField()
    nickname = models.TextField()
    age = models.IntegerField(default=25)
    gender = models.CharField(max_length=2, default='M')
    
#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        email=kwargs['email'],
        nickname=kwargs['nickname'],
        age=kwargs['age'],
        gender=kwargs['gender'],
    )

    return profile


class Ingredient(models.Model):
    name = models.TextField()

class Function(models.Model):
    name = models.TextField()