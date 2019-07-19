from django.db import models
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

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
    published_year = models.DateField(blank=True, null=True)
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
