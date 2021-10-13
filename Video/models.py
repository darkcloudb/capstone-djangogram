from django.db import models


class Vid(models.Model):
    username= models.CharField(max_length=50)
    vid_file= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.vid_file)

