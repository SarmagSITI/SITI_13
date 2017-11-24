from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class PostCategory(models.Model):
    category = models.CharField(max_length=100)
    created_date = models.DateTimeField(
    default = timezone.now
    )
    class Meta:
        ordering =['-created_date',]

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_category = models.ForeignKey(PostCategory, related_name="post_category")
    content = models.TextField()
    author = models.ForeignKey('auth.User')
    cover_image = models.ImageField(null=True, blank=True, upload_to='images/posts')
    created_date = models.DateTimeField(
        default = timezone.now
    )
    class Meta:
        ordering =['-created_date',]
