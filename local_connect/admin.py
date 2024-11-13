from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'account_type')