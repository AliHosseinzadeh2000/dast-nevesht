from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


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


class Comment(models.Model):
    user = models.CharField(max_length=200)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user
