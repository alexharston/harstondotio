from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404, HttpResponse
from django.utils import timezone
from .models import *
from .forms import PostForm
import os


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
    file_path = os.path.join(settings.SASS_PROCESSOR_ROOT, 'CV.pdf')
    #with open (file_path, 'rb') as pdf:
        #response = HttpResponse(pdf.read(), mimetype='application/pdf')
        #response['Content-Disposition'] = 'inline;filename=CV.pdf'
        #return response
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


def uses(request):
    uses = Use.objects.all()
    return render(request, 'uses.html', {'uses': uses})

def writing(request):
    posts = Post.objects.all().order_by('-published_date')
    books = Book.objects.all().order_by('-date_added')
    return render(request, 'writing.html', {'posts': posts, 'books': books})
