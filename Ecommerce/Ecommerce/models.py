from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone_number = models.DecimalField(max_digits=10)
    # shipping_address = models.TextField()
    # billing_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        abstract = True
