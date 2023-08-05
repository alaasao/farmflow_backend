from django.db import models

from django.contrib.auth.models import User
from choices import *

class Profile(models.Model):

    user=models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
    description=models.TextField(blank=True,null=True)
    type=models.CharField(choices=typechoices, max_length=50)
    specialty=models.CharField( max_length=50,blank=True,null=True)
    wilaya=models.CharField(choices=algerian_wilayas,max_length=50,blank=True,null=True)
    baladiya=models.CharField(choices=baladiyat, max_length=50,blank=True,null=True)
    likes_number=models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

from products.models import * 
class Like(models.Model):
    user=models.ForeignKey(Profile,   on_delete=models.CASCADE)
    product=models.ForeignKey(Product,   on_delete=models.CASCADE)
    def __str__(self):
        return self.user.user.username

class Card(models.Model):
    user=models.ForeignKey(Profile,   on_delete=models.CASCADE)
    product=models.ForeignKey(Product,   on_delete=models.CASCADE)
    def __str__(self):
        return self.user.user.username

