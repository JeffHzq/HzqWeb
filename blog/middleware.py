from django.shortcuts import render
from django.http import Http404

class BlogMiddleware:
    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return render(request, "404.html")