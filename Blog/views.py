from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("salam aleykom. this is first view for Blog app")