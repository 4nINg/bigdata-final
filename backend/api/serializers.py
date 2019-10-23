from .models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField('get_email')
    token = serializers.SerializerMethodField('get_token')
    is_authenticated = serializers.SerializerMethodField('get_is_authenticated')
    nickname = serializers.SerializerMethodField('get_nickname')
   
    class Meta:
        model = Profile
        fields = ('email', 'token', 'is_authenticated', 'nickname')

    def get_email(self, obj):
        return str(obj['username'])

    def get_token(self, obj):
        return str(obj['token'])
    
    def get_is_authenticated(self, obj):
        return obj['is_authenticated']

    def get_nickname(self, obj):
        return str(obj['nickname'])

