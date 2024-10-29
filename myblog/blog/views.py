from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm
from .models import Post, Category


def detail(request, category_slug, slug):
    '''
    View function to display the details of a specific blog post.

    Args:
        request (HttpRequest): The HTTP request object.
        category_slug (str): The slug of the category to which the post belongs to.
        slug (str): The slug of the specific blog post.

    Returns:
        HttpResponse: Renders the post detail template with the post and comment form.
    '''
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()


    return render(request, 'blog/detail.html', {'post': post, 'form': form})


def category(request, slug):
    '''
    View function to display all posts under a specific category.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the category.

    Returns:
        HttpResponse: Renders the category template with the category details.
    '''
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filer(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})