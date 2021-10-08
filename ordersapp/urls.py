import ordersapp.views as ordersapp
from django.urls import path

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='orders_list'),
    path('forming/complete/<pk>/',
            ordersapp.order_forming_complete, name='order_forming_complete'),
    path('create/', ordersapp.OrderItemsCreate.as_view(),
            name='order_create'),
    path('read/<pk>/', ordersapp.OrderRead.as_view(),
            name='order_read'),
    path('update/<pk>/', ordersapp.OrderItemsUpdate.as_view(),
            name='order_update'),
    path('delete/<pk>/', ordersapp.OrderDelete.as_view(),
            name='order_delete'),
]
]
