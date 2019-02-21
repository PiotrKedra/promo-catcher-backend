from django.urls import path

from app import views

urlpatterns = [
    path('users/', views.users, name='app_users'),
]