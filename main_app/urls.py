from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:user_name>', views.public_profile, name='public_profile'),
    path('signup/', views.signup, name='signup'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('accounts/login/', views.login, name='login'),
    path('cities/', views.cities, name='cities'),
    path('cities/<int:city_id>/', views.city_index, name='city_index'),
    path('cities/<int:city_id>/<int:post_id>',views.post, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('profile2/', views.profile2, name='profile2'),
]