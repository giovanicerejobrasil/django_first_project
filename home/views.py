# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    print('Function: home')
    return HttpResponse("<h1><em>HOME</em>: Bem vindo ao sistema!</h1>")
