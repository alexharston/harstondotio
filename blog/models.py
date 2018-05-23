from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Paper(models.Model):
    title = models.CharField(max_length=300)
    authors = models.TextField()
    published_date = models.IntegerField()
    abstract = models.TextField()
    url = models.TextField()
    doi = models.TextField()
    bodytext = models.TextField()

class Poster(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_year = models.DateField(blank=True, null=True)
    figures = MediaFile.objects


class Project(models.Model):
    title = models.TextField()
    background = models.TextField()
