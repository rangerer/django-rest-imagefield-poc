from django.shortcuts import render

from rest_framework import viewsets

from .models import TodoItem
from .serializers import TodoItemSerializer

# Create your views here.

class TodoItemViewset(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer