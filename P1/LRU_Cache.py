from collections import deque


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.size = capacity  # cache size = queue size
        self.hash = {}
        self.q = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hash:
            self.reorder_key(key)
            print(self.hash[key])
            return self.hash[key]
        else:
            print(-1)
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        if key not in self.hash:
            self.check_size()
            self.hash[key] = value
            self.q.append(key)
        else:
            self.reorder_key(key)

    def check_size(self):
        if len(self.q) == self.size:
            del self.hash[self.q.popleft()]

    def reorder_key(self, key):
        print('queue before reorder: ', self.q)
        self.q.remove(key)  # remove first occurence from queue
        self.q.append(key)  # append referenced key to the end of the queue
        print('queue after reorder: ', self.q)

our_cache = LRU_Cache(5)

our_cache.set(1, 'abba')
our_cache.set(2, 'baab')
our_cache.set(5, 'cappa')
our_cache.set(9, 'yippie')
our_cache.set(5, 'cappa')
our_cache.get(1)       # returns abba
our_cache.get(2)       # returns baab
our_cache.get(3)       # return -1