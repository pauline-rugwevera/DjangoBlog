from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# import readtime


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,
                                null=True)

    def __str__(self):
        return str(self.user)


class BlogPost(models.Model):
    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=130, unique=True)
    content = RichTextField(blank=True, null=True)
    image = CloudinaryField('image', default='placeholder')
    
    # def get_readtime(self):
    #     result = readtime.of_text(self.content)
    #     return result.text 


       
    


  
    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-dateTime']
  

    def __str__(self):
        return self.user.username + " Comment: " + self.content
