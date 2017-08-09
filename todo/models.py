from django.db import models
from datetime import datetime


class Todo(models.Model):
    title = models.CharField(max_length=200)
    prioridad = models.IntegerField()
    def __str__(self):
        return self.title