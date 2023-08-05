from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User,auth
from rest_framework.authtoken.models import Token
# from.models import Profile
from .serializers import UserSerializer

@csrf_exempt
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    print(user)
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data['username']})


from profiles.models import*
@api_view(['Post'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        profile=Profile.objects.create(user=user)
        profile.save()
      
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data['username']})
    return Response(serializer.errors)
@api_view(['Post'])
def logout(request):
 
    user=request.data['user']
    print(user)
    Token.objects.get(user=user).delete()
    return Response({"user":"loged out succesfuly"})