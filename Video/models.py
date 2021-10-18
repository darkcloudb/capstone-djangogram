from django.db import models
from Account.models import MyUser

class Vid(models.Model):
    username = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        )
    vid_file= models.FileField(upload_to='videos/', null=True, verbose_name="")
    posted_at = models.DateTimeField(auto_now_add=True)
    #favorite = models.ManyToManyField(MyUser, related_name='like')
    #likes = models.IntegerField(default=0)
    #dislikes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name + ": " + str(self.vid_file)

