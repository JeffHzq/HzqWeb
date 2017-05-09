from django.shortcuts import render
from django.http import Http404
from blog.models import *

def home(request):
    if request.method == 'GET':
        blogs = Blog.objects.order_by("-create_time").all()[:5]
        return render(request, 'home.html', {'blogs': blogs})
    else:
        raise Http404

def photo(request):
    return render(request, 'photo.html')


def func(request):
    return render(request, 'func.html')


def about(request):
    return render(request, 'about.html')


def relation(request):
    return render(request, 'relation.html')


def blog404(request):
    return render(request, '404.html')