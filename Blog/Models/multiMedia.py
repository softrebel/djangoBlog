from django.db import models
from Blog.models import Post


class MultiMedia(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    multiMedia = models.FileField(null=True, blank=True)
