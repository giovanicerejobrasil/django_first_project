from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # url estática e dinâmica
    # path('post/', views.blog, name='blog'),
    # path('post/<int:id>/', views.post, name='post'),

    path('', views.blog, name='blog'),
    path('post/<int:id>/', views.post, name='post'),
    path('example/', views.example, name='example'),
]
