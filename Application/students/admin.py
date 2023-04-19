from django.contrib import admin
from .models import Student
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_title = 'Kilimo High school'

admin_site = MyAdminSite()
admin.site.register(Student)
