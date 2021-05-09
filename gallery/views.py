from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

def home(request):
    return render(request, 'gallery/home.html')

def posts(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'gallery/post-detail.html', context)

def about(request):
    return render(request, 'gallery/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'gallery/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 12

class UserPostListView(ListView):
    model = Post
    template_name = 'gallery/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
