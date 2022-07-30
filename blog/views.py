from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Comment, Profile
from .forms import BlogPostForm, EditPostForm, UpdateProfileForm
from .forms import UpdateUserForm, CreateForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class PostList(ListView):
    model = BlogPost
    template_name = 'blog.html'
    ordering = ['-id']
    paginate_by = 3


class Create(SuccessMessageMixin, CreateView):
    # model = BlogPost
    model = CreateForm
    form_class = BlogPostForm
    template_name = 'create.html'
    success_message = 'Your post has been successfully created'

    def form_valid(self, form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
      homepage.
        """
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super().form_valid(form)


class UpdatePost(SuccessMessageMixin, UpdateView):
    model = BlogPost
    template_name = 'edit_post.html'
    form_class = EditPostForm
    success_message = 'Your post has been successfully updated'


class DeletePost(SuccessMessageMixin, DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = "Your post has been successfully deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)


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


@login_required
def profile(request):
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


#try out
# def Create(request):
#     """
#     renders share a recipe page
#     """
#     recipe_form = CreateForm(request.POST or None, request.FILES or None)
#     context = {
#         'recipe_form': recipe_form,
#     }

#     if request.method == "POST":
#         recipe_form = CreateForm(request.POST, request.FILES)
#         if recipe_form.is_valid():
#             print('valid')
#             recipe_form.instance.author = request.user
          
#             recipe = recipe_form.save(commit=False)

#             recipe.save()
#             return redirect('index')
#         else:
#             print('invalid')
#     else:
#         recipe_form = CreateForm()
#     return render(request, "creaate.html", context)
