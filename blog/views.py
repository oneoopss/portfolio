from django.shortcuts import render
from .models import Blog

def all_blogs(r):
    Blogs = Blog.objects.all()
    return render(r, 'blog/all_blogs.html', {'Blogs':Blogs})
