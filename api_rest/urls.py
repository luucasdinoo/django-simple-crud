from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<str:nick>', views.get_by_nick),
    path('data/', views.get_by_nick_with_param),
    path('user/create/', views.create_user),
    path('user/edit/', views.edit_user),
    path('user/edit/<str:nick>', views.edit_user2),
    path('user/delete/', views.delete_user),
    path('user/delete/<str:nick>', views.delete_user2),
]