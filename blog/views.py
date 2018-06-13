from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, InvalidPage
from django.core.paginator import PageNotAnInteger
from django.views import generic
from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin

from .models import Post, Commenter, Comment, Admin
from . import models


class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 1




class DetailView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 1


