from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost

class PostList(ListView):
    model = BlogPost
    template_name = 'blog.html'
    

class Create(CreateView):
    model = BlogPost
    fields = ('title', 'author', 'slug', 'content', 'image')
    template_name = 'create.html'




