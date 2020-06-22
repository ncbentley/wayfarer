from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post, City

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('full_name','username', 'email', 'current_city')

class EditProfileForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50)
    current_city = forms.CharField(max_length=50)
    class Meta:
        model = CustomUser
        fields = ('full_name', 'current_city')

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('city', 'title', 'content')

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class ImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('image',)