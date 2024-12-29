from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # url estática e dinâmica
    path('', views.blog, name='blog'),
    path('<int:post_id>/', views.post, name='post'),

    path('example/', views.example, name='example'),
]
