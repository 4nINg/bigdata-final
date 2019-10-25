from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from api.models import create_profile, Profile
from api.serializers import ProfileSerializer

from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

@api_view(['POST'])
def signup(request):
    params = request.data.get('params', None)
    email, password, nickname = params['email'], params['password'], params['nickname']
    age, gender = params['age'], params['gender']

    create_profile(username=email, password=password, age=age, 
                    nickname=nickname, email=email, gender=gender)

    return Response(status=status.HTTP_201_CREATED)

class CurrentUserAPIView(APIView):
    # authentication_classes = []
    # permission_classes = [AllowAny]
    def get(self, request):
        profile = Profile.objects.get(email=request.user)
        serializer = ProfileSerializer(profile)
    
        return Response(data=serializer.data, status=status.HTTP_200_OK)
