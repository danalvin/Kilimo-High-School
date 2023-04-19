from django.urls import path
from .views import register_student, student_list, student_detail, update_student, delete_student

urlpatterns = [
    path('register/', register_student, name='register_student'),
    path('', student_list, name='student_list'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', update_student, name='update_student'),
    path('delete/<int:pk>/', delete_student, name='delete_student'),

]
