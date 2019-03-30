from django.db import models
from Blog.models import Post


class News(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    lead = models.CharField(max_length=200, null=False)

