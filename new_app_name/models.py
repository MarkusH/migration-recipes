from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'rename_app_author'


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('new_app_name.Author')

    class Meta:
        db_table = 'rename_app_book'
