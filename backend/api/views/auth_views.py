from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from api.models import create_profile, Profile
from api.serializers import ProfileSerializer

from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

@api_view(['POST'])
def signup(request):
    params = request.data.get('params', None)
    print(params)
    email, password, nickname = params['email'], params['password'], params['nickname']
    age, gender = params['age'], params['gender']

    create_profile(username=email, password=password, age=age, 
                    nickname=nickname, email=email, gender=gender)


    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    params = request.data.get('params', None)
    email = params['email']
    password = params['password']

    user = authenticate(request, username=email, password=password)

    if user:
        auth.login(request, user)
        try:
            token = Token.objects.get(user=user)
        except Exception as e:
            token = Token.objects.create(user=user)
        request.session[str(token)]= email
        profile = Profile.objects.get(user=user)
        login_info = {
            'username':email,
            'token':token,
            'is_authenticated': True,
            'nickname': profile.nickname,
            }
    else:
        login_info = {
            'username': None,
            'token': None,
            'is_authenticated': None,
            'nickname': None,
            }
    
    serializer = ProfileSerializer(login_info)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

# 로그인 세션 유지 / 유저 정보 저장
@api_view(['POST'])
def session(request):
    params = request.data.get('params', None)
    token = params['token']
    email = request.session.get(token, None)
    if email == None:
        login_info = {
            'username': None,
            'token': None,
            'is_authenticated': None,
            'nickname': None,
            }
    else:
        user = User.objects.get(username=email)
        if user.is_authenticated and token == str(Token.objects.get(user=user)):
            profile = Profile.objects.get(user=user)
            login_info = {
                'username':email,
                'token':token,
                'is_authenticated': True,
                'nickname': profile.nickname,
            }
        else:
            login_info = {
                'username': None,
                'token': None,
                'is_authenticated': None,
                'nickname': None,
            }
    
    serializer = ProfileSerializer(login_info)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def logout(request):
    token = request.data.get('token', None)
    username = request.session.get(token, None)
    user = User.objects.get(username=username)

    del request.session[token]
    user.auth_token.delete()
    auth.logout(request)

    return Response(status=status.HTTP_200_OK)
