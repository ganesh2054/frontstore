from django.core import validators
from django.db import models
from django.db.models import fields
from django.core.validators import MinValueValidator

class Promotion(models.Model):
    description=models.CharField(max_length=255)
    discount=models.FloatField()

class Collection(models.Model):
    title=models.CharField(max_length=255)
    featured_product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+',blank=True)

    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering=['title']

class Product(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    description=models.TextField(null=True,blank=True)
    unit_price=models.DecimalField(max_digits=6,decimal_places=2,
    validators=[MinValueValidator(1)])
    inventory=models.CharField(max_length=255)
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotion,blank=True)
    active=models.BooleanField(null=False,default=False)
    trending=models.BooleanField(default=False)
    hot=models.BooleanField(default=False)
    product_image=models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering=['title']
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICE=[
        (MEMBERSHIP_BRONZE,'BRONZE'),(MEMBERSHIP_SILVER,'SILVER'),(MEMBERSHIP_GOLD,'GOLD')
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phon=models.CharField(max_length=255)
    last_update=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICE,default=MEMBERSHIP_BRONZE)
    def __str__(self) -> str:
     return self.first_name

    class Meta:
        ordering=['first_name']
  


class Order(models.Model):
    PAYMENT_STATUS_PENDING='P'
    PAYMENT_STATUS_COMPLETE='C'
    PAYMENT_STATUS_FAILED='F'
    PAYMENT_STATUS_CHOICE=[

        (PAYMENT_STATUS_PENDING,'Pending'),(PAYMENT_STATUS_COMPLETE,'Complete'),(PAYMENT_STATUS_FAILED,'Failed')
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICE,default=PAYMENT_STATUS_PENDING)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)
   

class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    zip=models.CharField(max_length=255)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)

class orderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
  



class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()

class Banner(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='images/')
    active=models.BooleanField(null=False,default=False)
    large=models.BooleanField(null=False,default=False)
  

class Photo(models.Model):
    product_image=models.ImageField(upload_to='images/')
    product=models.ForeignKey(Product,null=False,blank=False,on_delete=models.CASCADE)

class event(models.Model):
    title=models.CharField(max_length=255,null=False)
    description=models.TextField(max_length=255,null=True)
    price=models.DecimalField(max_digits=6,decimal_places=0)
    discount_price=models.DecimalField(max_digits=6,decimal_places=0)
    date=models.DateField()
    photo=models.ImageField(upload_to='images/',null=True)


