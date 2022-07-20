from django import forms
from .models import BlogPost


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
