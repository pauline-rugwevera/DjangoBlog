from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
from django.urls import reverse


class Profile:
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,
                                null=True)
    image = CloudinaryField('image', default='placeholder')
    bio = models.TextField(blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    Twitter = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class BlogPost(models.Model):
    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=130, unique=True)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('home')



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content