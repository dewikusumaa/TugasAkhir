from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Supplier

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'no_hp', 'address', 'created', 'updated']
    list_filter = ['created', 'updated']