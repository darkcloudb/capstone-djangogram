from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    # username = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.username
