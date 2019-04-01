from django.shortcuts import render
from django.http import HttpResponse
from djangoBlog.settings import BASE_DIR
from Blog.models import Post
from Blog.base import *
import json


def index(request):

    return HttpResponse("salam aleykom. this is first view for Blog app")


def about(request):
    return HttpResponse("kari az kusha")


def posts(request):
    postslist = Post.objects.all().order_by('-id')
    return render(request, 'post.html', {'posts': postslist})


if os.path.isdir(viewsPath):
    files = os.listdir(viewsPath)
    # mods=map(lambda file: import_file(file), files)
    for file in files:
        import_file(file,'views')
