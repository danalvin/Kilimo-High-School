# stream/urls.py

from django.urls import path
from . import views
from .views import AddStudentToStreamView, StreamDeleteView, StreamDetailView, StreamUpdateView

urlpatterns = [
    path('stream', views.StreamListView.as_view(), name='stream_list'),
    path('<slug:slug>/',views.StreamDetailView.as_view(), name='stream_detail'),
    path('new/', views.StreamCreateView.as_view(), name='stream_create'), 
    path('<slug:slug>/update/', StreamUpdateView.as_view(), name='stream_update'),
    path('<slug:slug>/delete/', StreamDeleteView.as_view(), name='stream_delete'),
    path('<slug:slug>/', StreamDetailView.as_view(), name='stream_detail'),
    path('<slug:slug>/assign/', AddStudentToStreamView.as_view(), name='stream_assign'),
]