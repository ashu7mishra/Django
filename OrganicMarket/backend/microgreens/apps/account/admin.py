from django.contrib import admin
from .models import CustomerUser


# admin.site.register(CustomerUser)


@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    fields = ["username", "phone", "address"]
    list_display = ["username", "phone"]
    search_fields = ["username", "phone", "address"]
