from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyUser(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.username
