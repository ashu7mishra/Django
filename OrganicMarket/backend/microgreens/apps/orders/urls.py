from django.urls import path
from .views import OrderListView, OrderDetailsView


# urlpatterns = [
#     path("", OrderListView.as_view(), name="order-list"),
#     path("<int:pk>", OrderDetailsView.as_view(), name="order-details"),
# ]