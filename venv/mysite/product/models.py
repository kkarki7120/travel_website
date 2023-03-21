
from django.db import models

from account.models import Guide, Customer

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
   
    
    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/')

    
    def __str__(self):
        return self.title
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    def __str__(self):
        return self.product.title

class Cart(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)

    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    
BOOK_STATUS = (
    ("Booking Received", "Booking Received"),
    ("Booking Processing", "Booking Processing"),
    ("Booking Completed", "Booking Completed"),
    ("Booking Canceled", "Booking Canceled"),
)


class Book(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    booked_by = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    book_status = models.CharField(max_length=50, choices=BOOK_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "Book: " + str(self.id)
