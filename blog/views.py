from django.shortcuts import render

# Create your views here.


def blog(request):
    context = {
        'content_title': 'BLOG: Hello, world!',
        'title': 'BLOG - ',
    }

    return render(
        request,
        "blog/index.html",
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
