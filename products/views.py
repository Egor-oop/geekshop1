from django.shortcuts import render
from products.models import ProductsCategory, Product


def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Geekshop - каталог',
        'products': Product.objects.all(),
        'categories': ProductsCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
