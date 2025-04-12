from django.db import models


class Task(models.model):
    name = models.CharField(max_length=100, unique=True)
    priority = models.IntegerField(default=0)
    executed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    