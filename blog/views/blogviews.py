# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import *

def blog(request):
    if request.method == 'GET':
        blogs = Blog.objects.order_by("-create_time").all()[:5]
        return render(request, 'blog.html', {'blogs': blogs})
    else:
        raise Http404

def content(request, blog_id):
    print blog_id
    if request.method == 'GET' and blog_id:
        blog = get_object_or_404(Blog, id=int(blog_id))
        return render(request, 'blog/content.html', {'blog': blog})
    else:
        raise Http404