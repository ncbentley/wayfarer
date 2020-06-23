from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime

# Create your models here.

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date_joined = models.DateField(default=timezone.now)
    current_city = models.CharField(max_length=50)
    image = models.ImageField(default='images/avatar.jpg', upload_to='images/profile_pics')

    REQUIRED = ['full_name', 'email', 'current_city']

    def __str__(self):
        return self.username

class City(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    content = models.TextField(max_length=4000)

    class Meta:
        ordering = ['-time']

class Comment(models.Model):
    time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)

    class Meta:
        ordering = ['-time']

