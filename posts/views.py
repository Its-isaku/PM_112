
#? Import necessary modules 
from django.views.generic import (ListView, DetailView, CreateView)
from .models import Post

#! |-------Define views for the Post model-------|

#? ListView to display a list of posts 
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    
#? DetailView to display a single post
class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    
    
#? CreateView to handle the creation of new posts
class PostCreateView(CreateView):
    template_name = "posts/create.html"
    model = Post
    fields = ['title', 'subtitle', 'body']


    