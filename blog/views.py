from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(r):
    blogs = Blog.objects.order_by('-date')
    return render(r, 'blog/all_blogs.html', {'blogs':blogs})

def detail(r, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(r, 'blog/detail.html',{'blog':blog})