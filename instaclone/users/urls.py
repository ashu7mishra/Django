from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="users_main_view"),
    path('signup/', views.signup, name="users_signup")
]