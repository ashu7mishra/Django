from django.db import models
from ...orders.models import Order


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('Razorpay', 'Razorpay'), ('Stripe', 'Stripe')])
    status = models.CharField(max_length=20, choices=[("Success", "Success"),
                                                      ("Failed", "Failed"), ("Pending", 'Pending')],
                              default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.transaction_id} - {self.status}"
