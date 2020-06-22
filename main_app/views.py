from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import CustomUserCreationForm, EditProfileForm, NewPostForm, EditPostForm

from .models import City, Post, CustomUser

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
        if request.user.is_authenticated:
            return redirect('cities')
        return render(request, 'home.html')

@login_required
def profile(request):
    posts = Post.objects.all().filter(user=request.user.id)
    context = {'edit_profile_form': EditProfileForm(initial={'full_name':request.user.full_name, 'current_city':request.user.current_city}), 'posts': posts, 'view_user': request.user}
    return render(request, 'registration/profile.html', context)

def public_profile(request, user_name):
    user = CustomUser.objects.get(username=user_name)
    posts = Post.objects.all().filter(user=user.id)
    context = {'view_user': user, 'posts': posts}
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

@login_required
def edit_profile(request):
    user = request.user
    form = EditProfileForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        user.full_name = request.POST.get('full_name')
        user.current_city = request.POST.get('current_city')
        user.save()
    return redirect('profile')

def cities(request):
    return redirect('/cities/1')

def city_index(request, city_id):
    city = City.objects.get(id=city_id)
    return redirect(f'/cities/{city.name.lower().replace(" ", "")}')

def city_index_by_name(request, city_name):
    cities = City.objects.all()
    for city in cities:
        if city.name.lower().replace(' ', '') == city_name:
            city_id = city.id
            posts = Post.objects.all().filter(city=city.id)
            break
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'city': city,
        'form': NewPostForm(),
        'page_obj': page_obj,
        'city_index': True
    }
    return render(request, 'cities/index.html', context)

def post_by_city_name(request, city_name, post_id):
    post = Post.objects.get(id=post_id)
    edit_post = EditPostForm(instance=post)
    context = {'post': post, 'image': post.city.name.lower().replace(' ', '-') + '.jpg', 'edit_post':edit_post}
    return render(request, 'cities/post.html', context)

def post(request, city_id, post_id):
    city = City.objects.get(id=city_id)
    return redirect(f'/cities/{city.name.lower().replace(" ", "")}/{post_id}')

@login_required
def create_post(request):
    form = NewPostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
    return redirect(f'/cities/{post.city.id}')

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user != request.user:
        return redirect(f'/cities/{post.city.id}/{post.id}')
    if request.method == 'POST':
        edit_post = EditPostForm(request.POST, instance=post)
        if edit_post.is_valid():
            edit_post.save()
            return redirect(f'/cities/{post.city.id}/{post.id}', post_id=post_id)

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user != request.user:
        return redirect(f'/cities/{post.city.id}/{post.id}')
    post.delete()
    return redirect(f'/cities/{post.city.id}')
    
# profile playground
def profile2(request):
    return render(request, 'registration/profile2.html')