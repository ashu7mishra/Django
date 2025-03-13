import threading
# from loadBalancerStrategies.roundRobin import RoundRobinStrategy
# from loadBalancerStrategies.leastConnections import LeastConnections
from ..models import Server


class LoadBalancerSingleton:
    _is_instance = None
    _lock = threading.Lock()

    def __new__(cls, strategy = 'round_robin'):
        if cls._is_instance is None:
            with cls._lock:
                if cls._is_instance is None:
                    cls._is_instance = super(LoadBalancerSingleton, cls).__new__(cls)
                    cls._is_instance.servers = []
                    cls._is_instance.strategy = strategy

        return cls._is_instance

    def add_server(self, server):
        LoadBalancerSingleton._is_instance.servers.append(server)

    def remove_server(self, server):
        LoadBalancerSingleton._is_instance.servers.remove(server)

    def distribute_request(self, request):
        if not LoadBalancerSingleton._is_instance.servers:
            return "No servers available"
        selected_server = LoadBalancerSingleton._is_instance.strategy.select_server(LoadBalancerSingleton._is_instance.servers)
        selected_server.handle_request(request)
        return selected_server

