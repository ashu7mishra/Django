from django.db import models
from task import Task

class Dependency(models.model):
    before = models.ForeignKey(Task, related_name='predecessor', on_delete=models.CASCADE)
    after = models.ForeignKey(Task, related_name='successor', on_delete=models.CASCADE)