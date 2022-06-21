from django.shortcuts import render

# from django.views import generic
from django.views.generic import ListView, DetailView
from .models import BlogPost

# class PostList(generic.ListView):
#     model = BlogPost
#     queryset = BlogPost.objects
#     template_name = 'blog.html'
class PostList(ListView):
    model = BlogPost
    template_name = 'blog.html'


