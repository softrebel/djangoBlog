from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
import os, importlib, importlib.util
from Blog.base import *


class Profile(AbstractBaseUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName=models.CharField(max_length=150,null=True)
    lastName=models.CharField(max_length=150,null=True)
    nationalCode= models.CharField(max_length=10,null=True)
    tellNumber= models.CharField(max_length=17,null=True)
    birthDate = models.DateTimeField(auto_now=True,null=False)
    avatar = models.ImageField(upload_to='profile', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=45,null=False)
    text=models.CharField(max_length=45,null=True)
    createdDate = models.DateTimeField(auto_now_add=False, auto_now=True)

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,db_index=True)
    createdDate = models.DateTimeField(auto_now_add=False, auto_now=True)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True)
    content = RichTextUploadingField(config_name='default')
    category=models.ForeignKey(Category, on_delete=models.DO_NOTHING,null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=False, auto_now=True)
    updateDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    publishDate = models.DateTimeField(auto_now_add=True)
    allowComment=models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/%Y-%m-%d', blank=True, null=True)

    def __str__(self):
        return '%s' % self.title



def import_file(file):
    path = modelsPath + os.sep + file
    if not os.path.isfile(path):
        return
    spec = importlib.util.spec_from_file_location("Blog.Models", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    globals().update(module.__dict__)


files = os.listdir(modelsPath)
# mods=map(lambda file: import_file(file), files)
for file in files:
    import_file(file)
