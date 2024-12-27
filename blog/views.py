# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog(request):
    print('Function: blog')
    return HttpResponse("<h1><em>BLOG</em>: Hello, world!</h1>")


def example(request):
    print(request)
    return HttpResponse("<h1><em>EXAMPLE</em>: Hello, world!</h1>")
