from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets,filters


# Create your views here.
class Viewsets_Products(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','owner__user__username','quantity','delevery_price']

class Viewsets_Categories(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
class Viewsets_Images(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ImageSerializer
class Viewsets_Review(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ReviewSerializer
class Viewsets_JobOffer(viewsets.ModelViewSet):
    queryset =  JobOffer.objects.all()
    serializer_class =  JobOfferSerializer
class Viewsets_Order(viewsets.ModelViewSet):
    queryset =  Order.objects.all()
    serializer_class =  OrderSerializer