from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date_joined = models.DateField(default=timezone.now)
    current_city = models.CharField(max_length=50)

    REQUIRED = ['full_name', 'email', 'current_city']

    def __str__(self):
        return self.username

CITIES = (
    ('san_francisco', 'San Francisco'),
    ('london', 'London'),
    ('sydney', 'Sydney'),
    ('seattle', 'Seattle')
)

class Form(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITIES, default=CITIES[0][0])
    content = models.TextField(max_length=1000)