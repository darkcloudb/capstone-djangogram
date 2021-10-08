from django.db import models
from Photo.models import PostImg
from django.contrib.auth.models import User
from Account.models import MyUser

class Comment(models.Model):
    post = models.ForeignKey(PostImg, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    # post = models.ManyToManyField(PostImg)
    # name = CharField()
    body = models.TextField()
    username = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.body
