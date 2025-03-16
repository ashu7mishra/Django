from django.urls import path
from .views import CacheView


urlpatterns = [
    path('<str:key/', CacheView.as_view(), name = 'cache-get'),
    path('', CacheView.as_view(), name = 'cache-put'),
    path('strategy', CacheView.as_view(), name = 'cache-strategy')
]