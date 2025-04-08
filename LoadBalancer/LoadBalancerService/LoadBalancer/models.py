from threading import Lock
from django.db import models


class Server(models.Model):
    def __init__(self):
        self.ip_address = models.GenericIPAddressField(unique=True)
        self.port = models.IntegerField()
        self.active_connections = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ip_address}: {self.port}"

    def handle_request(self, request):
        with Lock():
            self.active_connections += 1

        print(
            f"server with ip_address {self.ip_address} and port {self.port} "
            f"is processing request with {request.request_id} (active connections: {self.active_connections})"
        )

        with Lock():
            self.active_connections -= 1

        print(
            f"server with ip_address {self.ip_address} and port {self.port} "
            f"has processed request with {request.request_id} (active connections: {self.active_connections})"
        )


class Request(models.Model):
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="requests"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request to {self.server.ip_address}: {self.server.port}"

    def __init__(self, request_id):
        self.request_id = request_id
