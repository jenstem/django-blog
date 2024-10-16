from django.shortcuts import render
from blog.models import Post


def home_screen(request):
    posts = Post.objects.all()
    return render(request, 'personal/frontpage.html', {'posts': posts})


def about(request):
    return render(request, 'personal/about.html')
