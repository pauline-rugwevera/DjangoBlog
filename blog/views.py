from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from .models import BlogPost, Comment, Profile
from .forms import BlogPostForm, EditPostForm, ProfileForm, UpdateUserForm
from django.urls import reverse_lazy



from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.forms import UserChangeForm




class EditProfileView(generic.UpdateView):
    model = Profile
    form_class= ProfileForm
    template_name = 'edit_profile.html'
  
    success_url = reverse_lazy('home')


class PostList(ListView):
    model = BlogPost
    template_name = 'blog.html'
    ordering = ['-id']
    paginate_by = 3


#create post

class Create(SuccessMessageMixin, CreateView):
    model = BlogPost
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




@login_required
def profile(request):
    return render(request, "profile.html")



@login_required
def profile(request):
    """
    import required forms and create instances of those forms
    upon submission, it pass in the post data to the forms
    The user form expects an instance of a user while
    profile form we pass in an instance of the profile
    """
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        update_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if update_form.is_valid() and update_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:

        update_form  = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'update_form ': update_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)






# def user_profile(request, myid):
#     post = BlogPost.objects.filter(author=myid)
#     print(post)
#     return render(request, "user_profile.html", {'post':post})
   


def user_profile(request, myid):
    post = BlogPost.objects.filter(author=myid)
    print(post)
   
    return render(request, "user_profile.html", {'post':post})







