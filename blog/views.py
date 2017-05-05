from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def photo(request):
    return render(request, 'photo.html')

def func(request):
    return render(request, 'func.html')

def about(request):
    return render(request, 'about.html')

def relation(request):
    return render(request, 'relation.html')