from .baseStrategy import BaseStrategy


class LRUstrategy(BaseStrategy):

    def get(self, cache, key):
        if key in cache:
            cache.move_to_end(key)
            return cache[key]
        return None

    def put(self, cache, key, value, capacity):
        if key in cache:
            cache.move_to_end(key)
            cache[key] = value
        else:
            if len(cache) >= capacity:
                cache.popitem(last=False)
            cache[key] = value


