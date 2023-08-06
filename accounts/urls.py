from django.urls import re_path
from .views import login,signup,logout
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *
router = DefaultRouter()
router.register('users',Viewsets_Users)

urlpatterns = [
    
    re_path('crud/',include(router.urls)),

    re_path('login',login),
    re_path('signup',signup),
    re_path('logout',logout),
]