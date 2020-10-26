from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from .forms import PostForm


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})


def home(request):
    papers = Paper.objects.all()
    projects = Project.objects.all()
    posts = Post.objects.all().order_by('-published_date')
    posters = Poster.objects.all()

    context_dict = {
        'papers': papers, 
        'projects': projects, 
        'posts': posts,
        'posters': posters,
    }
    return render(request, 'home.html', context_dict)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def research(request):
    papers = Paper.objects.all().order_by('-year')
    return render(request, 'research.html', {'papers': papers})

def designs(request):
    designs = Design.objects.all()
    return render(request, 'designs.html', {'designs': designs})

def readinglist(request):
    readinglist = ReadPost.objects.all().order_by('-date_added')

def cv(request):
    return render(request, 'cv.html')

def uses(request):
    uses = Use.objects.all()
    return render(request, 'uses.html', {'uses': uses})

def downloads(request):
    files = File.objects.all()
    return render(request, 'download.html', {'files': files})

def writing(request):
    posts = Post.objects.all().order_by('-published_date')
    books = Book.objects.all().order_by('-date_added')
    return render(request, 'writing.html', {'posts': posts, 'books': books})
