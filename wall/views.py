# from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class BaseView(ListView):
    model = Post
    template_name = 'wall/post_list.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.order_by('-id')


class MapView(ListView):
    model = Post
    template_name = 'wall/map.html'
    context_object_name = 'map'

    def get_queryset(self):
        return Post.objects.order_by('-id')
