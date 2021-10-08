from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import transaction

from django.forms import inlineformset_factory

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from baskets.models import Basket
from ordersapp.models import Order, OrderItem
from ordersapp.forms import OrderItemForm


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
