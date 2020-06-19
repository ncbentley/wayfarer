from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import CustomUserCreationForm, EditProfileForm, NewPostForm

from .models import City, Post

# Create your views here.

def home(request):
    if request.method == 'POST':
        username_form = request.POST['username']
        password_form = request.POST['password']
        # authenticate user
        user = authenticate(username=username_form, password=password_form)
        if user is not None:
            # login
            login(request, user)
            #redirect
            return redirect('profile')
        else:
            return redirect(request.META.get('HTTP_ORIGIN') + '?login=fail')
    else:
        return render(request, 'home.html')

def profile(request):
    posts = Post.objects.all().filter(user=request.user.id)
    context = {'edit_profile_form': EditProfileForm(initial={'full_name':request.user.full_name, 'current_city':request.user.current_city}), 'posts': posts}
    return render(request, 'registration/profile.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            return redirect(request.META.get('HTTP_ORIGIN') + '?registration=fail')
    else:
        return redirect(request.META.get('HTTP_ORIGIN') + '?registration=fail')

def edit_profile(request):
    user = request.user
    form = EditProfileForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        user.full_name = request.POST.get('full_name')
        user.current_city = request.POST.get('current_city')
        user.save()
    return redirect('profile')

def cities(request):
    cities = City.objects.all()
    context = {}
    for city in cities:
        context[city.name.lower().replace(' ', '')] = Post.objects.all().filter(city=city.id)
    context['form'] = NewPostForm()
    context['city'] = 1
    return render(request, 'cities/index.html', context)

def city_index(request, city_id):
    cities = City.objects.all()
    context = {}
    for city in cities:
        context[city.name.lower().replace(' ', '')] = Post.objects.all().filter(city=city.id)
    context['form'] = NewPostForm()
    context['city'] = city_id
    return render(request, 'cities/index.html', context)

def post(request, city_id, post_id):
    post = Post.objects.get(id=post_id, city=city_id)
    context = {'post': post, 'image': post.city.name.lower().replace(' ', '-') + '.jpg'}
    return render(request, 'cities/post.html', context)

def create_post(request):
    form = NewPostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
    return redirect(f'/cities/{post.city.id}')