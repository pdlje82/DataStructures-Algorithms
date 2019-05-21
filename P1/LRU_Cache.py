"""
We use two data structures to implement an LRU Cache.

    1. Queue which is implemented using a python list. The maximum size of the queue will be equal to the
    total number of hash entries available (cache size).The most recently used items will be near the read
    end, and the least recent items will be near the front end.

         self.q = []
         len(self.q)          # size of the queue
         self.q.append(item)  # enqueue item at end of queue
         self.q.pop(0)        # dequeue item at front of queue

    2. A hash (dict) with page number as key and address of the corresponding queue node as value.
"""


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.size = capacity  # cache size = queue size
        self.hash = {}
        self.q = []

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hash:
            self.q.append(key)
            self.check_size()
            return self.hash[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        if key not in self.hash:
            self.hash[key] = value
        self.q.append(key)
        self.check_size()

    def check_size(self):
        if len(self.q) > self.size:
            del self.hash[self.q.pop(0)]


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1