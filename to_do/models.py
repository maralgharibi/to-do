from datetime import timezone

from django.db import models
from django.utils import timezone
def one_week():
    return timezone.now() + timezone.timedelta(days=7)
class Task(models.Model):
    id=models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(default=one_week())