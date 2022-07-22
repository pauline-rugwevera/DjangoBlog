from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Comment
from .forms import BlogPostForm, EditPostForm
from django.urls import reverse_lazy


class PostList(ListView):
    model = BlogPost
    template_name = 'blog.html'
    ordering = ['-id']
    paginate_by = 3


class Create(SuccessMessageMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create.html'
    success_message = 'Your post has been successfully created'


# update post
class UpdatePost(SuccessMessageMixin, UpdateView):
    model = BlogPost
    template_name = 'edit_post.html'
    form_class = EditPostForm
    success_message = 'Your post has been successfully updated'


# delete post
class DeletePost(SuccessMessageMixin, DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = "Your post has been successfully deleted"

    # delete messages
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)


# display detailed post,add comments
def post_detail(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog_id=post)
    if request.method == "POST":
        user = request.user
        content = request.POST.get('content', '')
        comment = Comment(user=user, content=content, blog_id=post)
        comment.save()
    return render(request, "post_detail.html",
                  {'post': post, 'comments': comments})


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        post = BlogPost.objects.filter(title__icontains=searched)
        return render(request, "search.html",
                      {'searched': searched, 'post': post})
    else:
        return render(request, "search.html", {})


