from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50, primary_key=True)


class Post(models.Model):
    title = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50, null=True)
