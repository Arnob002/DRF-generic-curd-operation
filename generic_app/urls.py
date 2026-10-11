from django.urls import path
from .views import *

urlpatterns = [
    path('students/',students.as_view(),name='students'),
    path('students/<str:pk>/',student_detail.as_view(),name='student_detail')
]