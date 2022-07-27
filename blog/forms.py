from django import forms
from .models import BlogPost, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        # fields = ('title', 'author', 'content', 'image')
        fields = ('title','content', 'image')
        widgets = {
            'title': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder':
                                             'Post Title'}),
          
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Post contents'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput
            (attrs={'class': 'form-control',
                             'placeholder': 'Post Title'}),
            'slug': forms.TextInput
            (attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Post contents'}),
        }






class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    facebook = forms.CharField(max_length=25,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

 
    linkedin = forms.CharField(max_length=25,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
 
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['facebook', 'linkedin', 'bio']