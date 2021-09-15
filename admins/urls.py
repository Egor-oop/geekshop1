from django.urls import path

from admins.views import index, UserListView, UserCreateView, admin_user_update, admin_users_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:id>/', admin_user_update, name='admin_user_update'),
    path('users-delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
]
