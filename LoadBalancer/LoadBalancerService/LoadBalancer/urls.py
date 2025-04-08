from django.urls import path
from .views import RegisterServerView, DistributeRequestView

urlpatterns = [
    path("register_server/", RegisterServerView.as_view(), name="register_server"),
    path(
        "distribute_request/",
        DistributeRequestView.as_view(),
        name="distribute_request",
    ),
]
