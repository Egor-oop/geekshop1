from django.urls import path

from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='product'),
    path('<int:category_id>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),
]
