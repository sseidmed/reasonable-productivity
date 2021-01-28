from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task 
        fields = ['title', 'description', 'created_at', 'updated_at']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

