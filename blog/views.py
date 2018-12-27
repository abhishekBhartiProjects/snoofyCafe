from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

posts = Post.objects.all()

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # - sign for reverse order

class PostDetailView(DetailView):
    model = Post #If we will stick to the naming convention, we will only require this single line of code.

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
