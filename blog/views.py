from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin
from .models import Post, Commenter, Comment, Admin
from . import models


class IndexView(PaginationMixin, ListView):

    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 3


class DetailView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 1
