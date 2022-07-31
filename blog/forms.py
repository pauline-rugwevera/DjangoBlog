from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from django.contrib.auth.models import User
from .models import BlogPost, Profile


# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ('title', 'content', 'image')
#         widgets = {
#             'title': forms.TextInput
#             (attrs={'class': 'form-control', 'placeholder':
#                                              'Post Title'}),
#             'content': forms.Textarea(attrs={'class': 'form-control',
#                                              'placeholder': 'Post contents'}),
#         }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'image')
        widgets = {
            'title': forms.TextInput
            (attrs={'class': 'form-control',
                             'placeholder': 'Post Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Post contents'}),
        }


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput
                               (attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', ]


class UpdateProfileForm(forms.ModelForm):
    linkedin = forms.CharField(max_length=30,
                               required=False,
                               widget=forms.TextInput
                               (attrs={'class': 'form-control'}))
    bio = forms.CharField(required=False, widget=forms.Textarea
                          (attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['linkedin', 'bio']


class BlogPostForm(forms.ModelForm):
    """
    Form class to add a recipe
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

  