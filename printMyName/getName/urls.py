from django.urls import path
from .views import print_name, add_student

urlpatterns = [
    path('name/<str:name>/', print_name),
    path('add_student/', add_student, name='add_student'),
]