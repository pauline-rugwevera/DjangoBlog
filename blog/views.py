from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import BlogPost, Comment
from .forms import BlogPostForm, EditPostForm, CommentForm

from django.urls import reverse_lazy

class PostList(ListView):
    model = BlogPost
    template_name = 'blog.html'
    ordering = ['-id']
    

class Create(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create.html'


# class PostDetailedView(DetailView):
#     model = BlogPost
#     template_name = 'post_detail.html'
#     form = CommentForm
#     slug_field = 'slug'

   

class UpdatePost(UpdateView):
    model = BlogPost
    template_name = 'edit_post.html'
    form_class = EditPostForm
    # fields = ['title', 'slug', 'content']


class DeletePost(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')    


def post_detail(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog_id=post)
    if request.method == "POST":
        user = request.user
        content = request.POST.get('content','')
        blog_id = request.POST.get('blog_id','')
        comment = Comment(user = user, content = content, blog_id=post)
        comment.save()
    return render(request, "post_detail.html", {'post': post,'comments':comments})









