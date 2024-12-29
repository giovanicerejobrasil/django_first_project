from django.shortcuts import render
from django.http import HttpRequest
from blog.data import posts
from typing import Any

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


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Exception('Post não existe!')

    context = {
        'title': f'BLOG - {found_post['title']}',
        'post': found_post
    }

    return render(
        request,
        'blog/post.html',
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
