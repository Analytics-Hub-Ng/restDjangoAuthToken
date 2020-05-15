from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # todo read more about this

from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)