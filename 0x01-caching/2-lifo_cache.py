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
        self.insertion_order = []
        super().__init__()

    def put(self, key, item):
        """
        store data in cache. manage memory with lifo
        algorithm
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.insertion_order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.insertion_order[-2]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        retrieve data from cache
        """
        self.insertion_order = []
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
