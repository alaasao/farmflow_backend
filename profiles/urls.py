from django.urls import path,include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profiles',Viewsets_Profiles)
router.register('card',Viewsets_Card)
router.register('like',Viewsets_Like)
urlpatterns = [
    
    path('crud/',include(router.urls))
]
