#!/usr/bin/env python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    caching system
    """

    def __init__(self):
        """
        inherit from BaseCace
        """
        super().__init__()

    def put(self, key, item):
        """
        insert data to cache_data
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        return value in cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
