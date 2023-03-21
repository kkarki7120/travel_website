from django.urls import path
from .import  views

urlpatterns=[
     path('',views.index, name='index'),
     path('register/',views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('guide_register/',views.guide_register.as_view(), name='guide_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('customer/', views.customer, name='customer'),
     path('add_product/', views.add_product, name='add_product'),
     path('gallery/', views.gallery, name='gallery'),
]