from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


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


def admin_user_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Geekshop - Редактирование пользователя',
        'selected_user': selected_user,
        'form': form,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)
