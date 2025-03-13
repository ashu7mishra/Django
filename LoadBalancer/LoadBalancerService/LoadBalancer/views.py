from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Request, Server
from .services.loadBalancer import LoadBalancerSingleton


class RegisterServerView(View):
    def post(self, request):
        ip_address = request.POST.get("ip_address")
        port = request.POST.get('port')
        server = Server.objects.create(i_address=ip_address, port=port)
        return JsonResponse({"message": "Server registered", "server_id": server.id})


class DistributeRequestView(View):
    def get(self, request):
        load_balancer = LoadBalancerSingleton()
        server = load_balancer.distribute_request(request)
        if server:
            request.objects.create(server=server)
            return JsonResponse({"message": "Request sent to server", "server": str(server)})
        return JsonResponse({"message": "No available servers"}, status=100)
