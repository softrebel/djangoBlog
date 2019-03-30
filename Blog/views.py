from django.shortcuts import render
from django.http import HttpResponse
from djangoBlog.settings import BASE_DIR


def index(request):
    return HttpResponse("salam aleykom. this is first view for Blog app")

def about(request):
    return HttpResponse("kari az kusha")