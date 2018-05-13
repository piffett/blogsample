import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    headline = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.TimeField('date published')

    def __str__(self):
        return self.headline


class Commenter(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Comment(models.Model):
    commenter = models.ForeignKey(Commenter, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)


class Admin(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
