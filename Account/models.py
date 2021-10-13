from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import IntegerField

# Create your models here.


class MyUser(AbstractUser):
    # username = models.ForeignKey('self', on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    age = IntegerField(default=0)
    prof_pic = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.username
