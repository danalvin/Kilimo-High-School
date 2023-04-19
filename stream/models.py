from django.db import models
from django.urls import reverse

from django.utils.text import slugify

class Stream(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField('students.Student', related_name='streams',)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Stream, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
