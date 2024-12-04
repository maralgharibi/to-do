from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect


from .models import Task
from .serializer import TodoSerializers

from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework.response import Response

class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TodoSerializers(tasks, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class TaskDetailView(APIView):
    def get_object(self,pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
    def get (self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TodoSerializers(task)
        return Response(serializer.data)
    def put(self,request,pk):
        task = self.get_object(pk)
        serializer = TodoSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



