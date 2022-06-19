from tkinter import CASCADE
from webbrowser import get
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# Create your models here.

# User = get_user_model()

SOURCE_CHOICES = (
    ('YT', 'Youtube'),
    ('Google', 'Google'),
    ('Newsletter', 'Newsletter'),
)

class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email