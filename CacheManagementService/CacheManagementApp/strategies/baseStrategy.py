from abc import ABC, abstractmethod


class BaseStrategy(ABC):

    @abstractmethod
    def get(self, cache, key):
        raise NotImplementedError

    @abstractmethod
    def put(self, cache, key, value, capacity):
        raise NotImplementedError
