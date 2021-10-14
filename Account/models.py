from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import IntegerField

# Create your models here.


class MyUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    bio = models.CharField(max_length=200)
    age = IntegerField(default=0, null=True, blank=True)
    prof_pic = models.ImageField(
        default='default.jpg', upload_to='pics/')
    email = models.EmailField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.username
