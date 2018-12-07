from django.shortcuts import render
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

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
