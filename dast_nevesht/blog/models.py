from distutils.command.upload import upload
import email
from pyexpat import model
from turtle import title
from venv import create
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)



class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    slug = models.SlugField(max_length=300,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)



    def __str__(self):
        return self.title







    
