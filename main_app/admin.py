from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser, City, Post

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['email', 'username', 'current_city',]

admin.site.register(City)
admin.site.register(Post)

admin.site.register(CustomUser, CustomUserAdmin,)