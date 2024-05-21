#!/usr/bin/env python3

""" BasicCache module that inherits from BaseCaching and is a caching system
Put method should be overrided and implement logic to assign
key and value in cache dictionary.
Get method should be overrided and implement logic to
return value linked to key.
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
    No limits on number of items it can store.
    """

    def __init__(self):
        """Initialize BasicCache
        """
        super().__init__()

    def put(self, key, item):
        """ Override put method and assign item value to the key in cache_data
        dictionary.
        If either key or item is None, do nothing.
        """
        if key is None or item is None:  # check if key and item are not None
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Override get method and return value linked to key in cache_data
        dictionary.
        If key is None or key does not exist in cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)  # return value associated with key
