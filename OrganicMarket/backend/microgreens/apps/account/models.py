from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.username


