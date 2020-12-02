import os
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello World')


def home(request):
    context={ }
    return render(request,'home.html',context)