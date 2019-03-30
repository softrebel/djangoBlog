from django.shortcuts import render
from django.http import HttpResponse
from djangoBlog.settings import BASE_DIR
from Blog.models import Post
import json

def index(request):

    return HttpResponse("salam aleykom. this is first view for Blog app")

def about(request):
    return HttpResponse("kari az kusha")

def posts(request):
    list = Post.objects.all().order_by('-id')[:2]
    return render(request, 'post.html', {'posts': list})
