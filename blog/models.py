from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.timezone import now
from ckeditor.fields import RichTextField

import readtime

from django.utils.text import slugify

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,
                                null=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)


    def __str__(self):
        return str(self.user)


class BlogPost(models.Model):
    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=130, unique=True)
    content = RichTextField(blank=True, null=True)
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('home')

    
    def get_readtime(self):
      result = readtime.of_text(self.content)
      return result.text

   
  
    
   


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-dateTime']
  

    def __str__(self):
        return self.user.username + " Comment: " + self.content
