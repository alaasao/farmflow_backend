from django.urls import path,include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products',Viewsets_Products)
router.register('categories',Viewsets_Categories)
router.register('products_images',Viewsets_Images)
router.register('reviews',Viewsets_Review)
router.register('joboffers',Viewsets_JobOffer)
router.register('orders',Viewsets_Order)

urlpatterns = [
    
    path('crud/',include(router.urls))
]
