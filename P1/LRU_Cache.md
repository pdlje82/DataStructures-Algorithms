
### LRU Chache
We use two data structures to implement an LRU Cache.

    1. Queue which is implemented using a python list.
       The maximum size of the queue will be equal to
       the total number of hash entries available
       (cache size).The most recently used items will
       be near the read end, and the least recent 
       items will be near the front end.

        self.q.append(key)              # enqueue item at end of queue O(1)
        self.q.pop(0)                   # dequeue item at front of queue O(1)
        key_index = self.q.index(key)
        self.q.pop(key_index)           # can both be considered O(1), as the cache 
                                        # size is small compared to the number of 
                                        # different key/value pairs

    2. A hash (dict) with ref.number as key and cached data as value.
       
        self.hash[key] = value          # add key/value to dict O(1)
        return self.hash[key]           # return value from dict (O(1)

