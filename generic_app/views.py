from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class students(generics.ListCreateAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentSerializers

# for take single obj in data
class student_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentSerializers
    lookup_field = 'pk'


