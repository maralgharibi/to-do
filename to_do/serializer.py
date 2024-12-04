from rest_framework import serializers
from .models import Task

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['title','description','is_completed','created_at','due_date']
