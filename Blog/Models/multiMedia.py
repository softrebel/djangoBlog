from django.db import models
from Blog.models import Post, File
from django.contrib.contenttypes.fields import GenericRelation


class MultiMedia(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    multiMedia = GenericRelation(File)
