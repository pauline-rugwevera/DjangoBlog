from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Comment, Profile
from .forms import BlogPostForm, EditPostForm, ProfileForm
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.forms import UserChangeForm



class UserEditView(SuccessMessageMixin, generic.UpdateView):
    form_class = ProfileForm
    
    template_name = 'edit_profile.html'
    success_message = 'Your profile has been succesfully updated'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


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



def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
     
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
 
        user = User.objects.create_user(username, email, password1)
      
        user.save()
        return render(request, 'loginn.html')  
    return render(request, "register.html")
    

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'blog.html')   
    return render(request, "loginn.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/loginn')


def user_profile(request, myid):
    post = BlogPost.objects.filter(id=myid)
    return render(request, "user_profile.html", {'post':post})

def Profile(request):
    return render(request, "profile.html")



# def edit_profile(request):
    
#     if request.method=="POST":
#         form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             alert = True
#             return render(request, "edit_profile.html", {'alert':alert})
#     else:
#         form=ProfileForm(instance=request.user.profile)
#     return render(request, "edit_profile.html", {'form':form})
