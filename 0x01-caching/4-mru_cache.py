#!/usr/bin/env python3

""" MRU cache module that inherits from BaseCaching and is a caching system
Must use self.cache_data - dictionary from the parent class BaseCaching
MRU algorithm must be used to manage the cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
    Uses MRU algorithm to manage cache.
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        # Initialize the access order list to
        # track the order of access to cache items
        self.access_order = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the
        item value for the key
        If key or item is None, do nothing.
        When number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS:
            - discard the most recently used item in self.cache_keys
            - discard the most recently used item in self.cache_data
        """
        if key is None or item is None:
            return
        # check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # discard most recently used item (MRU)
            # remove the most recently used key from access order
            mru_key = self.access_order.pop()
            # remove the corresponding item from cache data
            del self.cache_data[mru_key]
            # print the discarded key for debugging purposes
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item  # assign item to key in cache data
        self.access_order.append(key)  # add key to access order

    def get(self, key):
        """ Return value in self.cache_data linked to key
        If key is None or key does not exist in self.cache_data, return None
        """
        # if key is None or key not in self.cache_data:
        #     return None
        # return self.cache_data.get(key)
        if key is not None:  # check if key is not None
            if key in self.cache_data:  # if key exists in cache_data
                # update access order
                self.access_order.remove(key)
                self.access_order.append(key)
                return self.cache_data[key]  # return value associated with key
        return None  # return None if key is None or key not in cache_data
