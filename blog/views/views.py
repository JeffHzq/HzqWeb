from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse
from blog.models import *
from django.views.decorators.http import require_GET, require_POST
import json
from django.core.serializers import serialize
from django.http import request

@require_GET
def get_blogs(request):
    try:
        page = int(request.GET.get('page', 1))
        num = int(request.GET.get('num', 5))
        blogs = Blog.objects.order_by("-create_time").all()[(page-1)*num:page*num]
        # jsondata = json.dumps(list(blogs))
        jsondata = serialize('json', blogs, ensure_ascii=False)
    except Exception, e:
        print e.message
    return HttpResponse(jsondata, content_type="application/json")

@require_GET
def home(request):
    try:
        blogs = Blog.objects.order_by("-create_time").all()[:5]
    except Exception, e:
        print e.message
    return render(request, 'home.html', {'blogs': blogs})

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
