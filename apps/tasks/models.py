from core.models import BaseModel
from django.db import models


class Task(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name
