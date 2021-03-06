# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 07:49
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    Author = apps.get_model('alter_pk', 'Author')
    Post = apps.get_model('alter_pk', 'Post')

    author1 = Author.objects.create(name='Author 1')
    author2 = Author.objects.create(name='Author 2')
    Post.objects.create(title='Title 1.1', author=author1)
    Post.objects.create(title='Title 2.1', author=author1)
    Post.objects.create(title='Title 1.2', author=author2)
    Post.objects.create(title='Title 2.2', author=author2)


def backwards(apps, schema_editor):
    Author = apps.get_model('alter_pk', 'Author')
    Author.objects.filter(name='Author 1').delete()
    Author.objects.filter(name='Author 2').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('alter_pk', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
