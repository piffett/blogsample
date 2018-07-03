from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views


app_name = 'blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', views.DetailView.as_view(), name='detail'),

]

