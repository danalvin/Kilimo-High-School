from django.core.management.base import BaseCommand
from students.models import Student

class Command(BaseCommand):
    help = 'Populate the database with initial student data'

    def handle(self, *args, **kwargs):
        students = [
            {'name': 'John Doe', 'date_of_birth': '2005-06-01', 'grade_level': 11},
            {'name': 'Jane Smith', 'date_of_birth': '2004-07-15', 'grade_level': 12},
            {'name': 'Bob Johnson', 'date_of_birth': '2006-02-28', 'grade_level': 10},
            # add more student data as needed
        ]

        for student_data in students:
            student = Student(**student_data)
            student.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated database with student data.'))