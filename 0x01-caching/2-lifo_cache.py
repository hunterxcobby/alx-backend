#!/usr/bin/env python3

""" LIFO cache module that inherits from BaseCaching and is a caching system
Must use self.cache_data - dictionary from the parent class BaseCaching
LIFO algorithm must be used to manage the cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
    Uses LIFO algorithm to manage cache.
    """

    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the
        item value for the key
        If key or item is None, do nothing.
        When number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS:
            - discard the last item in self.cache_keys
            - discard the last item in self.cache_data
        """
        if key is None or item is None:
            return
        # check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.cache_keys.pop()  # discard last item (LIFO)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.cache_keys.append(key)
        self.cache_data[key] = item  # assign item to key in cache_data

    def get(self, key):
        """ Return value in self.cache_data linked to key
        If key is None or key does not exist in self.cache_data, return None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
