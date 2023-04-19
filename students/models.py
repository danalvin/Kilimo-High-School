from django.db import models

from stream.models import Stream

class Student(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    grade_level = models.IntegerField()
    enrollment_date = models.DateField(auto_now_add=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='students_enrolled', null=True, blank=True)

    
    def __str__(self):
        return self.name
