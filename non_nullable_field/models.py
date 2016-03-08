from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    @classmethod
    def create(cls, name):
        return cls.objects.create(name=name)
