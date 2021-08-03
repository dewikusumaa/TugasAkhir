from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('delete/<int:id>/', views.deleteUser),
    path('update/<int:id>/', views.updateUser),
    path('create/', views.createUser),
    path('daftar/', views.users),
]