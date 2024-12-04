from django.contrib import admin
from .models import Task

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'is_completed', 'created_at']
    list_filter = ['is_completed']
    search_fields = ['title']

admin.site.register(Task, TodoAdmin)