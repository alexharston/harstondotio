from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
    'published_date').reverse()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def research(request):
    return render(request, 'research.html')

def designs(request):
    return render(request, 'designs.html')

def pay(request):
    return render(request, 'pay.html')

def cv(request):
    return render(request, 'cv.html')