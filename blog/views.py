from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Comment, Profile
from .forms import BlogPostForm, EditPostForm, CommentForm, ProfileForm
from django.urls import reverse_lazy

# from django.contrib.auth.forms import UserChangeForm

# read post
class PostList(ListView):
    model = BlogPost
    template_name = 'blog.html'
    ordering = ['-id']
    
# create post
class Create(SuccessMessageMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create.html'
    success_message = 'Post successfully created'
  
    
# class EditUserView(UpdateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'edit_profile.html'
#     success_url = reverse_lazy('home') 
#     success_message = 'Post successfully created'


# class PostDetailedView(DetailView):
#     model = BlogPost
#     template_name = 'post_detail.html'
#     form = CommentForm
#     slug_field = 'slug'

   
# update post
class UpdatePost(SuccessMessageMixin, UpdateView):
    model = BlogPost
    template_name = 'edit_profile.html'
    form_class = EditPostForm
    success_message = 'Post successfully updated'
    # fields = ['title', 'slug', 'content']


# edit user profile
# class EditUserView(CreateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'edit_profile.html'
#     success_url = reverse_lazy('home') 
#     success_message = 'Post successfully created'


# delete post
class DeletePost(SuccessMessageMixin, DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home') 
    success_message = "Post has been successfully deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)


# display detailed post,add comments
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

# show user profile
def user_profile(request, myid):
    post = BlogPost.objects.filter(id=myid)
    return render(request, "user_profile.html", {'post':post})

def Profile(request):
    return render(request, "profile.html")


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        post = BlogPost.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'post':post})
    else:
        return render(request, "search.html", {})
