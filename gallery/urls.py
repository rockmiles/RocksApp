from django.urls import path
from .views import PostListView, UserPostListView, PostCreateView
from . import views

urlpatterns = [
    path('home', views.home, name='home-page'),
    path('', PostListView.as_view(), name='post-page'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='about-page')
]
