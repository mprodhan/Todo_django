from django.db import models
from django.utils import timezone
from todo_user.models import TodoUser

class Todo(models.Model):
    todo = models.CharField(max_length=60)
    note = models.TextField(blank=True, null=True)
    posted = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    todo_user = models.ForeignKey(on_delete=models.CASCADE)

    def __str__(self):
        return self.todo


