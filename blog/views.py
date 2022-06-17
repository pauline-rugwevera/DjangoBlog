from django.shortcuts import render

from django.views import generic, View
from .models import BlogPost

class PostList(generic.ListView):
    model = BlogPost
    template_name = 'blog.html'


