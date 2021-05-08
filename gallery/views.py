from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def home(request):
    return render(request, 'gallery/home.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'gallery/post-detail.html', {'posts' : posts})

def about(request):
    return render(request, 'gallery/about.html')
