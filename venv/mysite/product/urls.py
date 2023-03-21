from django.urls import path
from .import  views

urlpatterns=[
     
     path('add_product/', views.add_product, name='add_product'),
     path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
     path('guide/', views.guide, name='guide'),
     path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
     path('<slug:category_slug>/', views.category, name='category'),
     path('search/', views.search, name='search'),
]