from django.db import models
from django.utils.html import format_html


class Author(models.Model):
    name = models.CharField(max_length=50)
    homepage = models.URLField()

    @classmethod
    def create(cls, name, homepage):
        return cls.objects.create(name=name, homepage=homepage)

    @property
    def homepage_tag(self):
        return format_html(
            '<a href="{homepage}">{homepage}</a>',
            homepage=self.homepage,
        )
