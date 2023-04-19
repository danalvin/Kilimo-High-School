# stream/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('stream', views.StreamListView.as_view(), name='stream_list'),
    path('<int:stream_id>/',views.StreamDetailView.as_view(), name='stream_detail'),
    path('new/', views.StreamCreateView.as_view(), name='stream_create'),
    path('<int:stream_id>/edit/', views.StreamUpdateView.as_view(), name='stream_edit'),
    path('<int:stream_id>/delete/', views.StreamDeleteView.as_view(), name='stream_delete'),
    path('<int:stream_id>/assign/', views.assign_students, name='assign_student'),
]
