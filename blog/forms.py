from django import forms
from .models import BlogPost, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'author', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder':
                                             'Post Title'}),
            'slug': forms.TextInput
            (attrs={'class': 'form-control',
             'placeholder':
                    'Copy the title with no space and a hyphen in between'}),
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
            (attrs={'class': 'form-control',
             'placeholder':
                    'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Post contents'}),
        }


class ProfileForm(forms.ModelForm):

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))





    class Meta:
        model = User
     
        fields = ('username', 'email')