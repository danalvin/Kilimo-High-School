from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'grade_level']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'date_of_birth', 'grade_level', 'enrollment_date')