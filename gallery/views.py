from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'gallery/home.html')

def postdetail(request):
    return render(request, 'gallery/post-detail.html')
