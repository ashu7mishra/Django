from django.contrib import admin
from .models import CustomerUser


# admin.site.register(CustomerUser)


@admin.register(CustomerUser)
class UserCustomer(admin.ModelAdmin):
    fields = ["username", "phone", "address"]
