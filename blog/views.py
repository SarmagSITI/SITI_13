from django.shortcuts import render
from .models import Post, PostCategory
from .forms import PostForm, CategoryPostForm
# Create your views here.
def index(request):
    context={}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'blog/category.html', context)

def addpost(request):
    return render(request, 'blog/addpost.html')

def postlist(request):
    return render(request, 'blog/post_list.html')

def postdetail(request):
    return render(request, 'blog/post_detail.html')
