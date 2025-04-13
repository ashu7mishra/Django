from .views import *
from django.urls import path


urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/dependency/', DependencyView.as_view()),
    path('scheduler/run/', SchedulerRunView.as_view()),
]