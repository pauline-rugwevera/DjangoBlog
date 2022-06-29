from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import BlogPost
from .forms import BlogPostForm

class PostList(ListView):
    model = BlogPost
    template_name = 'blog.html'
    

class Create(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create.html'


class PostDetailedView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'


class UpdatePost(UpdateView):
    model = BlogPost
    template_name = 'edit_post.html'
    fields = ['title', 'slug', 'content']





   










