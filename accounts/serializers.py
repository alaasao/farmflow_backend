from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import Profile
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']
    def validate_email(self, value):
        """
        Check if the email is already taken by an existing user.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model=User
        fields ='__all__'
        