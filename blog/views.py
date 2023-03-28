from django.shortcuts import render
from .models import Blog

def all_blogs(r):
    blogs = Blog.objects.order_by('-date')[:2]
    return render(r, 'blog/all_blogs.html', {'blogs':blogs})
