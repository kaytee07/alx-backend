#!/usr/bin/env python3
"""
FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines FIFOCache
    - where our data will be stored
    - how to retrieve data from the cache
    """
    def __init__(self):
        """
        inherit Parent class BaseCaching
        """
        self.insertion_order = []
        super().__init__()

    def put(self, key, item):
        """
        store data into cache
        """
        if key is None or item is None:
            return
        self.insertion_order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            new_key = self.insertion_order[0]
            del self.cache_data[new_key]
            print(f"DISCARD: {new_key}")
            self.insertion_order.pop(0)

    def get(self, key):
        """
        return value linked to key in cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
