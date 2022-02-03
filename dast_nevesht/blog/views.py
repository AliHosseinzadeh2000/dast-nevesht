from msilib.schema import ListView
from turtle import update
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post 
from django.views.generic.detail import DetailView


class PostListView(ListView):
    template_name = 'home.html'
    queryset = Post.objects.order_by('-updated_at')[:10]


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p1 = Post.objects.get(pk=self.kwargs['pk']) 
        context['comment_list'] = p1.comment_set.all()
        return context