from .baseStrategy import BaseStrategy
from collections import Counter


class LFUstrategy(BaseStrategy):

    def __init__(self):
        self.frequency = Counter()

    def get(self, cache, key):
        if key in cache:
            self.frequency[key] += 1
            return cache[key]
        return None

    def put(self, cache, key, value, capacity):
        if key in cache:
            cache[key] = value
            self.frequency[key] += 1
        else:
            if len(cache) >= capacity:
                least_frequent = min(self.frequency, key=self.frequency.get)
                cache.pop(least_frequent, None)
                self.frequency.pop(least_frequent, None)
            cache[key] = value
            self.frequency[key] += 1