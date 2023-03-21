from django.contrib import admin
from .models import Book, Cart, CartProduct, Category, Product, ProductImage

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(CartProduct)
admin.site.register( Cart)
admin.site.register( Book)


