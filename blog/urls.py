from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views


app_name = 'blog'
urlpatterns = [
    path('top/', views.IndexView.as_view(), name='blog'),
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    url(r'^', views.DetailView.as_view(), name='detail'),

]

