from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost
from .forms import BlogPostForm

class PostList(ListView):
    model = BlogPost
    template_name = 'blog.html'
    

class Create(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    # fields = ('title', 'author', 'slug', 'content', 'image')
    template_name = 'create.html'




