from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('blog/', include('blog.urls')),
    url(r'^accounts/', include('register.urls')),
]
