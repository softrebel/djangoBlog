from django.db import models
from Blog.models import Post,Tag


class PostTags(models.Model):
    id=models.AutoField(primary_key=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=False, auto_now=True)
