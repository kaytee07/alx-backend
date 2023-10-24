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
        super().__init__()

    def put(self, key, item):
        """
        store data into cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            new_key, new_value = self.cache_data.popitem()
            print(f"DISCARD: {new_key}")

    def get(self, key):
        """
        return value linked to key in cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
