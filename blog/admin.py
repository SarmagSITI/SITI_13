from django.contrib import admin
from .models import PostCategory, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title',]
admin.site.register(Post, PostAdmin)

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory
    list_display = ['category', 'created_date',]
admin.site.register(PostCategory, PostCategoryAdmin)
