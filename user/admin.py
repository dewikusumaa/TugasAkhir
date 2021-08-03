from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'password', 'level', 'created', 'updated']
    list_filter = ['created', 'updated']