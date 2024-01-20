from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Task
from .serializers import TaskSerializer


class TaskListCreatAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskGetPutDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
