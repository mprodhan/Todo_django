from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class TodoUser(AbstractUser):
    display_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.display_name
