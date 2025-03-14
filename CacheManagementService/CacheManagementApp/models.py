from django.db import models


class CacheEntry(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    frequency = models.IntegerField(default=0)  # used for LFU
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.key}: {self.value}"
