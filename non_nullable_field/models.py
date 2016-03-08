from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class Author(models.Model):
    name = models.CharField(max_length=50)
    homepage = models.URLField(null=True)

    @classmethod
    def create(cls, name, homepage):
        return cls.objects.create(name=name, homepage=homepage)

    @property
    def homepage_tag(self):
        if self.homepage:
            return format_html(
                '<a href="{homepage}">{homepage}</a>',
                homepage=self.homepage,
            )
        return mark_safe('<i>No homepage</i>')
