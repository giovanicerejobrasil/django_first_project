from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'text': 'HOME: Hello, world!',
        'title': 'HOME - ',
    }

    return render(
        request,
        'home/index.html',
        context,
    )
