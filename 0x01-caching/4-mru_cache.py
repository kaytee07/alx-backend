#!/usr/bin/env python3
"""
LIFO module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    storing, retrieving data in cache. remove data from cache when
    memory is full
    """
    def __init__(self):
        """
        inherit data from BaseCaching parent class
        """
        self.recently_used = []
        super().__init__()

    def put(self, key, item):
        """
        store data in cache. manage memory with mru
        algorithm
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            recent_key = ""
            if len(self.recently_used) == 0:
                recent_key = list(self.cache_data.keys())[-2]
            else:
                recent_key = self.recently_used[-1]
            del self.cache_data[recent_key]
            print(f"DISCARD: {recent_key}")
            if len(self.recently_used) > 0:
                self.recently_used.pop()

    def get(self, key):
        """
        retrieve data from cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.recently_used = []
        self.recently_used.append(key)
        return self.cache_data[key]
