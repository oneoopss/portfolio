from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=200)
    text = models.TextField()
