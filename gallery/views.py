from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def home(request):
    return render(request, 'gallery/home.html')

def postdetail(request):
    posts = Post.objects.all()
    return render(request, 'gallery/post-detail.html', {'posts' : posts})
