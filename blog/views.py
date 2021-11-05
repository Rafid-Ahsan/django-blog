from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.newManager.all()

    return render(request, 'index.html', {
        'posts': posts
    })
