from django.db import models

from django.contrib.auth.models import User
from choices import *
from phonenumber_field.modelfields import PhoneNumberField
class MonthYearField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(7)'

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value.strftime('%Y-%m')

    def to_python(self, value):
        if isinstance(value, str):
            return value
        return value.strftime('%Y-%m')
class Profile(models.Model):

    user=models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
    description=models.TextField(blank=True,null=True)
    type=models.CharField(choices=typechoices, max_length=50)
    specialty=models.CharField( max_length=50,blank=True,null=True)
    wilaya=models.CharField(choices=algerian_wilayas,max_length=50,blank=True,null=True)
    baladiya=models.CharField(choices=baladiyat, max_length=50,blank=True,null=True)
    likes_number=models.IntegerField(default=0)
    phone=PhoneNumberField(blank=True,null=True)
    card_number=models.IntegerField(blank=True, null=True)
    expiration_date=MonthYearField(blank=True, null=True)
    name_on_card=models.CharField(blank=True, null=True, max_length=50)
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

