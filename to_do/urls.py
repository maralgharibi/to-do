from .views import TaskListView,TaskDetailView
from django.urls import path
urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]