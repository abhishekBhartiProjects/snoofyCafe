from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

posts = Post.objects.all()

# posts = [
#     {
#         'author': 'Abhishek',
#         'title': 'First Blog Post',
#         'content': 'First blog content',
#         'date_posted': 'December 6, 2018',
#     },
#     {
#         'author': 'Varsha',
#         'title': 'Second Blog Post',
#         'content': 'Second blog content',
#         'date_posted': 'December 6, 2018',
#     }
#
# ]

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

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
