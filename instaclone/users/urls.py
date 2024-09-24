from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="user_main_view")
]