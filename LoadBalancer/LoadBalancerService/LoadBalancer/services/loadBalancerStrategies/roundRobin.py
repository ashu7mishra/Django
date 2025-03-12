from abc import ABC
from ..baseStrategy.baseStrategy import LoadBalancingStrategy


class RoundRobinStrategy(LoadBalancingStrategy):

    def __init__(self, servers):
        self.index = 0
        self.servers = servers

    def select_server(self):
        server = self.servers[self.index % len(self.servers)]
        self.index += 1
        return server

