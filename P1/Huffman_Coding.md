### Runtime Complexity for Hoffman Encoding and Decoding

create node for each character and push to heap: O(n) \
build tree: O(n) \
traversing the tree to build codes: O(n log n) \
decode using a dict (hash): O(1) \
\
Overall performance encoding: O(n log(n))\
Overall performance decoding: O(1)
