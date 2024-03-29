from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Comment, Profile
from .forms import BlogPostForm, EditPostForm, UpdateProfileForm
from .forms import UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class PostList(ListView):
    """view to create the post on the blog"""
    model = BlogPost
    template_name = 'blog.html'
    ordering = ['-id']
    paginate_by = 6


class Create(SuccessMessageMixin, CreateView):
    """view to create the post on the blog"""
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create.html'
    success_message = 'Your post has been successfully created'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super(Create, self).form_valid(form)


class UpdatePost(SuccessMessageMixin, UpdateView):
    """view to edit the post on the blog"""
    model = BlogPost
    template_name = 'edit_post.html'
    form_class = EditPostForm
    success_message = 'Your post has been successfully updated'


class DeletePost(SuccessMessageMixin, DeleteView):
    """view to delete the post on the blog"""
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = "Your post has been successfully deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)


def post_detail(request, slug):
    """renders post detail"""
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog_id=post)
    if request.method == "POST":
        user = request.user
        content = request.POST.get('content', '')
        comment = Comment(user=user, content=content, blog_id=post)
        comment.save()
    return render(request, "post_detail.html",
                  {'post': post, 'comments': comments})


@login_required
def profile(request):
    """create,update user profile"""
    profile = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES,
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile is updated successfully')
            return redirect(to='/')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form,
                                            'profile_form': profile_form})
