from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin

from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.DetailView.as_view(), name='detail'),
    path('top', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]

