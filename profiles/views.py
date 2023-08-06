from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets,filters



class Viewsets_Profiles(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user']
class Viewsets_Like(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class =LikeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__id','product__id']
class Viewsets_Card(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['user__id','product__id']
