from django.db import models
from Photo.models import PostImg
from django.contrib.auth.models import User

class Comment(models.Model):
    comment = models.ForeignKey(PostImg, related_name='comments', on_delete=models.CASCADE)
    # name = CharField()
    body = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
