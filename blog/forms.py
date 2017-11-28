from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import Textarea
from .models import Post, PostCategory

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Judul',required=True)
    content = forms.CharField(label='Deskripsi', widget=forms.Textarea, required=True)
    image = forms.ImageField(label = 'Gambar', required=False)

    class Meta:
        model = Post
        fields = ('title','content','image','post_category')

class CategoryPostForm(forms.ModelForm):

    class Meta:
        model = PostCategory
        fields = ('category',)
