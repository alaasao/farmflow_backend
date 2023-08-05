from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta(object):
        model=Profile
        fields ='__all__'
        
class LikeSerializer(serializers.ModelSerializer):
  
    class Meta(object):
        model=Like
        fields ='__all__'
        
class CardSerializer(serializers.ModelSerializer):
 
    class Meta(object):
        model=Card
        fields ='__all__'
        