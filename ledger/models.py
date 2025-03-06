from django.db import models

# Create your models here.

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)
    
class Task(models.Model):
    name = models.CharField(max_length=50)
    isCompleted = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey(TaskGroup, on_delete=models.CASCADE)