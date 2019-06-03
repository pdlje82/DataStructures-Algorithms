Design choice
A python dict is used with collections.counter for fast character counting and 
fast access. Python heapq is used to build a sorted list with fast access on 
both sides (push and pop)

### Runtime Complexity for Hoffman Encoding and Decoding

create node for each character and push to heap: O(n) \
build tree: O(n) \
traversing the tree to build codes: O(n log n) \
decode using a dict (hash): O(1) \
\
Overall performance encoding: O(n log(n))\
Overall performance decoding: O(1)

### Space Coplexity
O(n)
