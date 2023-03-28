from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False,)
