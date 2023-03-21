import random
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from account.models import *
from .models import  Product, Category

from .forms import ProductForm, ProductImageForm

@login_required
def guide(request):
    guide = request.user.guide
    products = guide.products.all()
    return render(request,'guides.html', {'guide': guide, 'products': products} )

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.guide = request.user.guide
            product.slug = slugify(product.title)
            product.save()

            return redirect('guide')
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})

@login_required
def edit_product(request, pk):
    guide = request.user.guide
    product = guide.products.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        image_form = ProductImageForm(request.POST, request.FILES)

        if image_form.is_valid():
            productimage = image_form.save(commit=False)
            productimage.product = product
            productimage.save()

            return redirect('guide')

        if form.is_valid():
            form.save()

            return redirect('guide')
    else:
        form = ProductForm(instance=product)
        image_form = ProductImageForm()
    
    return render(request, 'edit_product.html', {'form': form, 'image_form': image_form, 'product': product})



def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)



    return render(request, 'product.html', {'similar_products':similar_products})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'category.html', {'category':category})


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'products': products, 'query': query})