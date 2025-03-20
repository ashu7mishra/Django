from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="customeruser_groups",  # Custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="customeruser_permissions",  # Custom related_name
        blank=True
    )

    def __str__(self):
        return self.username


