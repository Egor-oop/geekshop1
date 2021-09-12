from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm


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


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()

    context = {
        'title': 'Geekshop - Создание пользователя',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)
