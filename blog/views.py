# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog(request):
    print('Function: my_view')
    return HttpResponse("<h1><em>BLOG</em>: Hello, world!</h1>")
