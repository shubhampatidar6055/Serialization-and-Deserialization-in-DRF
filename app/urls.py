from django.urls import path
from .models import *
from app import views

urlpatterns = [
    path("", views.student_detail),
    path("student_create", views.student_create),
]
