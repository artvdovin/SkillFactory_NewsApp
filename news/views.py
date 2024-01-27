from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.

class News (ListView):
    model = Post
    ordering = '-date_add'
    template_name = 'news.html'
    context_object_name = 'news'


class Post (DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
