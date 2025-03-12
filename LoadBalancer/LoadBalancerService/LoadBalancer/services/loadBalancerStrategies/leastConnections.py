from ..baseStrategy.baseStrategy import LoadBalancingStrategy


class LeastConnections(LoadBalancingStrategy):
    def __init__(self, servers):
        self.servers = servers

    def select_server(self):
        min_connections = float('inf')
        selected_server = None

        for server in self.servers:
            if server.active_connections < min_connections:
                min_connections = server.active_connections
                selected_server = server
        return selected_server
