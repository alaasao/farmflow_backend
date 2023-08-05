from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model=ProductCategory
        fields ='__all__'
        
class ImageSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model=ProductImage
        fields ='__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta(object):
        model=Product
        fields ='__all__'
        

class ReviewSerializer(serializers.ModelSerializer):

    class Meta(object):
        model=ProductReview
        fields ='__all__'
class  JobOfferSerializer(serializers.ModelSerializer):

    class Meta(object):
        model= JobOffer
        fields ='__all__'
class  OrderSerializer(serializers.ModelSerializer):

    class Meta(object):
        model= Order
        fields ='__all__'
        