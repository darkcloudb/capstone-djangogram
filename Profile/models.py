from django.db.models.fields import IntegerField
from Account.models import MyUser
from django.db import models
from Photo.models import PostImg

# Create your models here.


class Profile(models.Model):
    myuser = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    images = models.ImageField(
        PostImg,
        default='default.jpg',
        upload_to='profile_pics')
    bio = models.CharField(max_length=100)
    age = IntegerField()

    def __str__(self):
        return(self.myuser)
