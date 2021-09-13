from django.contrib import admin

from products.models import ProductsCategory, Product

admin.site.register(ProductsCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
