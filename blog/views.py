from django.shortcuts import render
from blog.data import posts

# Create your views here.


def blog(request):
    context = {
        'title': 'BLOG - ',
        'content_title': 'BLOG: Hello, world!',
        'posts': posts,
    }

    return render(
        request,
        "blog/index.html",
        context
    )


def post(request, id):
    context = {
        'title': 'BLOG - ',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def example(request):
    context = {
        'content_title': 'EXAMPLE: Hello, world!',
    }

    return render(
        request,
        "blog/example.html",
        context
    )
