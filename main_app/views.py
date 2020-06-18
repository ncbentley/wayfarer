from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'registration/profile.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            return redirect(request.META.get('HTTP_ORIGIN') + '?registration=fail', {'error_message': 'Invalid signup please try again'})
    else:
        return redirect(request.META.get('HTTP_ORIGIN') + '?registration=fail')

