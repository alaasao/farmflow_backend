from django.db import models
from profiles.models import Profile
from profiles.location import *
from choices import *
class ProductCategory(models.Model):
    main_category=models.CharField(max_length=20,verbose_name=("category name"),null=True,blank=True)
    parent_cat=models.ForeignKey('self',limit_choices_to={'parent_cat__isnull':True},on_delete=models.CASCADE,null=True,blank=True,verbose_name=("parent category"))

    def __str__(self):
        return str(self.main_category)
    class Meta:
        verbose_name=('category')
      
class Product(models.Model):
    # Seller or service provider offering the product or service
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # State whether the object is a product or a service and specify the type of service
    status = models.CharField(choices=status, max_length=50)

    # Name of the product or service
    name = models.CharField(max_length=50)

    # Unit of measurement for selling the product (e.g., kg, quantity) or payment for the service (e.g., per hours, per days)
    selling_unit = models.CharField(choices=unitchoices, max_length=50)

    # Price per unit for the product or service
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2)

    # Quantity of the product available (depends on the unit of measurement) for the service it will be how many hours or days you need the service for
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    # Description of the product or service (optional)
    description = models.TextField(blank=True, null=True)

    # Status indicating if the product is sold only in big quantities (optional)  it will be null for services
    selling_status = models.CharField(choices=sellingchoices, max_length=50, blank=True, null=True)

    # Minimum quantity for selling the product (optional)  it will be null for services
    min_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # Whether the service provider brings their equipment (optional) it will be for products
    equipements = models.BooleanField(blank=True, null=True)

    # Date and time of product creation (auto-generated)
    creation_date = models.DateTimeField(auto_now_add=True)

    # Category of the product or service
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    # Location: Wilaya (province) where the product or service is offered (optional)
    wilaya = models.CharField(choices=algerian_wilayas, max_length=50, blank=True, null=True)

    # Location: Baladiya (local municipality) where the product or service is offered (optional)
    baladiya = models.CharField(choices=baladiyat, max_length=50, blank=True, null=True)

    # Delivery range option for the product (default: no delivery) or working area for services
    delivery_range = models.CharField(choices=delivery, max_length=50, default="no delivery")

    # Delivery price for the product (default: 0)  it will be null for services
    delivery_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)   
    def __str__(self) :

        return self.name
def get_image_upload_path(instance):
    return f"Products/{instance.status}/{instance.name}" 
class ProductImage(models.Model):
    #we used a model for image and not field in case the product or the sevice has many imges
    Product=models.ForeignKey(Product, on_delete=models.CASCADE)
    main_image=models.BooleanField(default=False)
    image=models.ImageField(upload_to=get_image_upload_path, height_field=None, width_field=None, max_length=None)
class ProductReview(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    review=models.TextField()
class JobOffer(models.Model):
    recruiter=models.ForeignKey(Profile,  on_delete=models.CASCADE)
    job_description=models.TextField()
    payment=models.DecimalField( max_digits=5, decimal_places=2)
    wilaya=models.CharField(choices=algerian_wilayas, max_length=50,blank=True,null=True)
    baladiya=models.CharField(choices=baladiyat,max_length=50,blank=True,null=True)

class Order(models.Model):
    # Connects the order to the seller (service provider or product seller)
    seller=models.ForeignKey(Profile,  on_delete=models.CASCADE,related_name="done_purchases")
    # Connects the order to the buyer (service requester or product buyer)
    buyer=models.ForeignKey(Profile,  on_delete=models.CASCADE)
    # Represents the ordered quantity or for how long the service is needed, based on the payment unit
    quantity=models.DecimalField( max_digits=5, decimal_places=2)
    # Represents the address where the product should be delivered or service provided
    addresse=models.CharField( max_length=50)
    
    