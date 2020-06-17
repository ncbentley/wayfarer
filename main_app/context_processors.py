from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_form(request):
    return {
        'login_form': AuthenticationForm()
    }

def registration_form(request):
    return {
        'registration_form': UserCreationForm()
    }