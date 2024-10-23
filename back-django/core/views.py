from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def blog_view(request) -> HttpResponse:
    posts: BaseManager[Post] = Post.objects.all()
    return render(request, 'core/blog.html', {'posts': posts})
