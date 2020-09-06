from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.published_date = timezone.now() 
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Paper(models.Model):

    title = models.CharField(max_length=300)
    authorlist = models.CharField(max_length=512, null=True)
    journal = models.CharField(max_length=1000, null=True)
    year = models.IntegerField(null=True)
    link = models.URLField(default="")
    doi = models.CharField(max_length=1000, blank=True, default='')
    abstract = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Poster(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    published_year = models.DateField(blank=True, null=True)
    _file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title


class Project(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    link = models.URLField(default="")


    def __str__(self):
        return self.title

class Design(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    published_year = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return self.title


class ReadPost(models.Model):

    title = models.TextField(max_length=500)
    link = models.URLField(default="")
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Book(models.Model):

    title = models.CharField(max_length=500)
    author = models.CharField(max_length=300, default="")
    link = models.URLField(default="", blank=True, null=True)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Use(models.Model):

    CATEGORIES= [
        ['Development', 'Development'],
        ['Productivity', 'Productivity'],
        ['Equipment', 'Equipment'],
    ]
    title = models.CharField(max_length=500)
    description = models.TextField(default="")
    category = models.TextField(default="", choices=CATEGORIES)

    def __str__(self):
        return self.title