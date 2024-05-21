#!/usr/bin/env python3

""" LFU cache module that inherits from BaseCaching and is a caching system
Must use self.cache_data - dictionary from the parent class BaseCaching
LFU algorithm must be used to manage the cache.
If you find more than one item to discard,
use the LRU algorithm to manage the cache.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching
    Uses LFU algorithm to manage cache.
    And swicthes to LRU algorithm if more than one item to discard.
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()  # Call parent's __init__ method
        self.access_order = []  # Track order of access
        self.frequency = {}  # Track the frequency of each key

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the
        item value for the key
        If key or item is None, do nothing.
        When number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS:
            - discard the least frequently used item in self.cache_keys
            - discard the least frequently used item in self.cache_data
        """
        if key is None or item is None:
            return
        # check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # find the key(s) with minimum frequency
            min_freq = min(self.frequency.values())
            # get the key(s) with minimum frequency
            least_frequent_keys = [k for k, v in self.frequency.items()
                                   if v == min_freq]
            # if there is more than one key with same minimum frequency
            if len(least_frequent_keys) > 1:
                # use LRU algorithm to discard least recently used key
                lru_key = self.access_order.pop(0)
                # remove the least recently used key from access order
                self.access_order.remove(lru_key)
                # remove the least recently used key from cache data
                del self.cache_data[lru_key]
                # remove the least recently used key from frequency
                del self.frequency[lru_key]
                print(f"DISCARD: {lru_key}")
            else:  # only one key with minimum frequency
                # discard the least frequently used item
                lfu_key = least_frequent_keys[0]
                # remove the least frequently used key from access order
                self.access_order.remove(lfu_key)
                # remove the least frequently used key from cache data
                del self.cache_data[lfu_key]
                # remove the least frequently used key from frequency
                del self.frequency[lfu_key]
                print(f"DISCARD: {lfu_key}")
        self.cache_data[key] = item  # assign item to key in cache data
        # update frequency of key
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ Return value in self.cache_data linked to key
        If key is None or key does not exist in self.cache_data, return None
        """
        if key is not None:  # check if key is not None
            if key in self.cache_data:  # if key exists in cache_data
                # Update frequency
                self.frequency[key] += 1
                if key in self.access_order:
                    self.access_order.remove(key)
                self.access_order.append(key)
            return self.cache_data[key]  # return value associated with key
        return None  # return None if key is None or key not in cache_data
