from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

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
