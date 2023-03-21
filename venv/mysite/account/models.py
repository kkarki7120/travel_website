from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser





class User(AbstractUser):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    is_customer = models.BooleanField('Is customer', default=False)
    is_guide = models.BooleanField('Is guide', default=False)
    
    
    
    
    
   
     
class Customer(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    country = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    

    def __str__(self):
        return self.first_name

    
   

class Guide(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    date_of_birth = models.DateField(null=True)
    country = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    work_experience = models.CharField(max_length=250,null=True)
    
   
    def __str__(self):
        return self.first_name
    
   
