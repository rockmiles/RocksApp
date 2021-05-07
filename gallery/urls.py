from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home-page'),
    path('', views.posts, name='post-page')
]
