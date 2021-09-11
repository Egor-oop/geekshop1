from django.urls import path

from admins.views import index, admin_users

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
]
