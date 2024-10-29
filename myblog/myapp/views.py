from django.shortcuts import render
from blog.models import Post


def home_screen(request):
    '''
    View function that handles requests to the home screen.

    Retrieves all posts from the database and renders them on the front page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page with posts.
    '''
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'personal/frontpage.html', {'posts': posts})


def about(request):
    '''
    View function that handles requests to the about page.

    Renders the about page without any additional context.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page for the about section.
    '''
    return render(request, 'personal/about.html')
