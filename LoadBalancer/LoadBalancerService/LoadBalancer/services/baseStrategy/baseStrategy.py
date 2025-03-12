from abc import ABC, abstractmethod


class LoadBalancingStrategy(ABC):

    @abstractmethod
    def select_server(self):
        raise NotImplementedError
