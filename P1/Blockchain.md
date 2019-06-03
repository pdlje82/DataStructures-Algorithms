### Design choice for BLockchain
The Blockchain is created using a linked list for saving the previous hash 
in each block. Also, for fast access, a python dict is used to store the hashes as 
keys and the corresponding blocks itself as values.

### Runtime Complexity for simple Blockchain algorithm

Calculate hash O(1)
Append block to Block (traverse the entire chain once) O(n)
print Blockchain: O(n)

Overall: O(n)

### Space Commplexity:

O(n) for linked list and python dict