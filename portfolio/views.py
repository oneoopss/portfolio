from django.shortcuts import render
from .models import Project

def home(r):
    projects = Project.objects.all()
    return render(r, 'portfolio/home.html', {'projects':projects})