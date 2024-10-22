from django.shortcuts import get_object_or_404, render
from .forms import CommentForm
from .models import Post


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'form': form})