from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    library = models.ForeignKey('Library')


class Library(models.Model):
    name = models.CharField(max_length=200)
