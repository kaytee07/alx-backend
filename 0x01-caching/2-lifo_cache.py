#!/usr/bin/env python3
"""
LIFO module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    storing, retrieving data in cache. remove data from cache when
    memory is full
    """
    def __init__(self):
        """
        inherit data from BaseCaching parent class
        """
        super().__init__()

    def put(self, key, item):
        """
        store data in cache. manage memory with lifo
        algorithm
        """
        insertion_order = []
        if key is None or item is None:
            return
        self.cache_data[key] = item
        insertion_order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = insertion_order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        retrieve data from cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
