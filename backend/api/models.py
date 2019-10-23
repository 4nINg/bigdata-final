from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

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

class Product(models.Model):
    name = models.TextField() # 제품명
    company_name = models.TextField() # 회사명
    ingredient_list = JSONField() # 주성분 리스트
    product_to_ingredient = models.ManyToManyField(Ingredient, related_name="ingredient_to_product") # 성분 M:N
    product_to_function = models.ManyToManyField(Function, related_name="function_to_product") # 효능 M:N
    heavy_metal = JSONField() # 중금속 리스트
    intake_hint = models.TextField()  # 섭취힌트
    intake_method = models.TextField() # 섭취방법
    preservation = models.TextField() # 보존방법
    distrbution = models.TextField() # 유통기한
    image_url = models.TextField() # 이미지url
    views = models.IntegerField(default=0) # 조회수


# class Comment(models.Model):
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)