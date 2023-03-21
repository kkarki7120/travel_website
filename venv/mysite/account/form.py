from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction

from .views import *
from .models import User,Customer,Guide

from django.forms import ModelForm

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    country = forms.CharField(required=True)
    city = forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.country=self.cleaned_data.get('country')
        customer.city=self.cleaned_data.get('city')
        customer.save()
        return user

class GuideSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    country = forms.CharField(required=True)
    city = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True)
    work_experience = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_guide = True
        user.firtst_name = self.cleaned_data.get('full_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        guide = Guide.objects.create(user=user)
        guide.firtst_name = self.cleaned_data.get('first_name')
        guide.last_name = self.cleaned_data.get('last_name')
        guide.phone_number=self.cleaned_data.get('phone_number')
        guide.country=self.cleaned_data.get('country')
        guide.city=self.cleaned_data.get('city')
        guide.date_of_birth=self.cleaned_data.get('date_of_birth')
        guide.work_experiece=self.cleaned_data.get('work_experience')

        guide.save()
        return user
 
