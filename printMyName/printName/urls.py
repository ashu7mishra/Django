from django.urls import path
from .views import print_name

urlpatterns  = [
    path('name/', print_name)
]