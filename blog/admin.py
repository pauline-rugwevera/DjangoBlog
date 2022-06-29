from django.contrib import admin
from .models import BlogPost, Comment
from django_summernote.admin import SummernoteModelAdmin



admin.site.register(Comment)

@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = 'content'


