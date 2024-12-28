from django.shortcuts import render

# Create your views here.


def blog(request):
    context = {
        'text': 'BLOG: Hello, world!',
        'title': 'BLOG - ',
    }

    return render(
        request,
        "blog/index.html",
        context
    )


def example(request):
    context = {
        'text': 'EXAMPLE: Hello, world!',
    }

    return render(
        request,
        "blog/example.html",
        context
    )
