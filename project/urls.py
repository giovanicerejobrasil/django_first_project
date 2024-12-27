"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# HTTP Request <-> HTTP Response
# Django trabalha com MVT uma variação do MVC


def home(request):
    print('Function: home')
    return HttpResponse("HOME: Bem vindo ao sistema!")


def my_view(request):
    print('Function: my_view')
    return HttpResponse("BLOG: Hello, world!")


urlpatterns = [
    path('', home),
    path('blog/', my_view),
    path('admin/', admin.site.urls),
]
