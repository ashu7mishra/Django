from django.contrib import admin
from .models import Category, Product


# admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Category)
class UserCategory(admin.ModelAdmin):
    fields = ["name"]


@admin.register(Product)
class UserProduct(admin.ModelAdmin):
    fields = ["name", "price", "stock", "description"]
