from collections import OrderedDict
from ..strategies.LFUstrategy import LFUstrategy
from ..strategies.LRUstrategy import LRUstrategy
from threading import Lock


class CacheManager:
    _instance = None

    def __new__(cls, capacity=5, strategy="LRU"):
        if cls._instance is None:
            with Lock():
                if cls._instance is None:
                    cls._instance = super(CacheManager, cls).__new__(cls)
                    cls._instance.capacity = capacity
                    cls._instance.cache = OrderedDict()
                    cls._instance.strategy = (
                        LRUstrategy() if strategy == "LRU" else LFUstrategy()
                    )
        return cls._instance

    def get(self, key):
        return self.strategy.get(self.cache, key)

    def put(self, key, value):
        self.strategy.put(self.cache, key, value, self.capacity)

    def set_strategy(self, strategy):
        try:
            self.strategy = LRUstrategy() if strategy == "LRU" else LFUstrategy()
            print(f"strategy set to {strategy['strategy']}")
        except Exception as e:
            print(f"No such strategy ({strategy['strategy']}) found", e)
