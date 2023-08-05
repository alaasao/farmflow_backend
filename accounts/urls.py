from django.urls import re_path
from .views import login,signup,logout
urlpatterns=[
    re_path('login',login),
    re_path('signup',signup),
    re_path('logout',logout),
]