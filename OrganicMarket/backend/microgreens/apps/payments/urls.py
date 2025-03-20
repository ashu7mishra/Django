from django.urls import path
from .views import PaymentInitiateView, PaymentStatusView


# urlpattern = [
#     path("initiate/", PaymentInitiateView.as_view(), name='payment-initiate'),
#     path("status/", PaymentStatusView.as_view(), name='payment-status'),
# ]