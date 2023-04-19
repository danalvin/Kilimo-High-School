from django.db import models
from django.urls import reverse

class Stream(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField('students.Student')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stream_detail', args=[str(self.id)])