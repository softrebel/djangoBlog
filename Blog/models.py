from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from ckeditor_uploader.fields import RichTextUploadingField
from Blog.base import *
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class Profile(AbstractBaseUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=150, null=True)
    lastName = models.CharField(max_length=150, null=True)
    nationalCode = models.CharField(max_length=10, null=True)
    tellNumber = models.CharField(max_length=17, null=True)
    birthDate = models.DateTimeField(auto_now=True, null=False)
    avatar = models.ImageField(upload_to='profile', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)


class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='files/%Y-%m-%d')
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.CharField(max_length=50)
    content_object = GenericForeignKey('content_type', 'object_id')


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    text = models.CharField(max_length=45, null=True)
    createdDate = models.DateTimeField(auto_now_add=False, auto_now=True)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, db_index=True)
    createdDate = models.DateTimeField(auto_now_add=False, auto_now=True)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True)
    content = RichTextUploadingField(config_name='default')
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=False, auto_now=True)
    updateDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    publishDate = models.DateTimeField(auto_now_add=True)
    allowComment = models.BooleanField(default=True)
    image = GenericRelation(File)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return '%s' % self.title


if os.path.isdir(modelsPath):
    files = os.listdir(modelsPath)
    # mods=map(lambda file: import_file(file), files)
    for file in files:
        import_file(file, 'models')
