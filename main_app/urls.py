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
    path('cities/<str:city_name>/', views.city_index_by_name, name='city_index_by_name'),
    path('cities/<str:city_name>/<int:post_id>', views.post_by_city_name, name='post_by_city_name'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('cities/<str:city_name>/<int:post_id>/comments/', views.post_comments, name='post_comments')
]