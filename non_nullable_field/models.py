from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    homepage = models.URLField(null=True)

    @classmethod
    def create(cls, name):
        return cls.objects.create(name=name)
