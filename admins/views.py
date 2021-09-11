from django.shortcuts import render

from users.models import User


def index(request):
    context = {
        'title': 'Geekshop - Admin'
    }
    return render(request, 'admins/index.html', context)


def admin_users(request):
    context = {
        'title': 'Geekshop - Пользователи',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users.html', context)
