from django.db import models


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()


class Commenter(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)


class sCommenter(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    auth_code = models.CharField(max_length=50)
    register_date = models.DateField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.cascade)
    commenter = models.ForeignKey(Commenter, on_delete=models.cascade)
    content = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=50)
    article = models.ManyToManyField(Article)


