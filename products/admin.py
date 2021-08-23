from django.contrib import admin

from products.models import ProductsCategory, Product

admin.site.register(Product)
admin.site.register(ProductsCategory)