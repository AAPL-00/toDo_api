from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [ 'title', 'description', 'completed']
        read_only_fields = ['created_at', 'updated_at']
