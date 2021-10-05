from django.db import models
from django.contrib.auth.models import User
from Account.models import MyUser

# Create your models here.

class PostImg(models.Model):
    image = models.ImageField(upload_to='pics/')
    body = models.CharField(max_length=50)
    username = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        )
    posted_at = models.DateTimeField(auto_now_add=True)
    favorite = models.ManyToManyField(User, related_name='like')
    comment = models.TextField()

    def __str__(self):
        return self.body
