# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import *
from django.views.decorators.http import require_GET

@require_GET
def blog(request):
    data = {}
    if 'type' in request.GET:
        blogs =Blog.objects.filter(type=int(request.GET['type'])).order_by("-create_time").all()[:5]
        data['type'] = get_object_or_404(BlogType, id=int(request.GET['type']))
    else:
        blogs = Blog.objects.order_by("-create_time").all()[:5]
    data['blogs'] = blogs
    return render(request, 'blog.html', data)

@require_GET
def content(request, blog_id):
    if blog_id:
        blog = get_object_or_404(Blog, id=int(blog_id))
        return render(request, 'blog/content.html', {'blog': blog})
    else:
        raise Http404