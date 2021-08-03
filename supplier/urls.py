from django.urls import path
from . import views

app_name = 'supplier'

urlpatterns = [
    path('delete/<int:id>/', views.deleteSupplier),
    path('create/', views.addSupplier),
    path('list/', views.suppliers),
]