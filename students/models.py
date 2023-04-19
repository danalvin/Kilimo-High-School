from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    grade_level = models.IntegerField()
    enrollment_date = models.DateField(auto_now_add=True)
