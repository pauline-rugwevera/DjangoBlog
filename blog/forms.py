from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from django.contrib.auth.models import User
from .models import BlogPost, Profile


class BlogPostForm(forms.ModelForm):
    """
    Form class to add a post
    """
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'image',
        ]

        widgets = {
            'content': SummernoteWidget(),
        }


class EditPostForm(forms.ModelForm):
    """
    Form class to edit a post
    """

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'image')
        widgets = {
            'content': SummernoteWidget(),
        }


class UpdateUserForm(forms.ModelForm):
    """Form class to update userprofile"""
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput
                               (attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', ]


class UpdateProfileForm(forms.ModelForm):
    """Form class to update profile"""
    linkedin = forms.CharField(max_length=30,
                               required=False,
                               widget=forms.TextInput
                               (attrs={'class': 'form-control'}))
    bio = forms.CharField(required=False, widget=forms.Textarea
                          (attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['linkedin', 'bio']
