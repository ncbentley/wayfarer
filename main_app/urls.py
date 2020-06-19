from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('accounts/login/', views.login, name='login'),
    path('cities/', views.cities, name='cities'),
    path('cities/<int:city_id>/', views.city_index, name='city_index'),
    path('cities/<int:city_id>/<int:post_id>',views.post, name='post'),
]