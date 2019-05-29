import hashlib
import time


class Block:

    def __init__(self, data):
        self.timestamp = None
        self.data = data
        self.previous_hash = None
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_time(self):
        return self.timestamp


class Blockchain:

    def __init__(self):
        self.head = None
        self.last = None
        self.map = {}  # save hashes and respective blocks

    def append(self, block):
        # if head, set previous to None
        if self.head is None:
            self.head = block
        # link to previous hash
            block.previous_hash = None
        else:
            block.previous_hash = self.last.hash
        # add timestamp
        block.timestamp = time.time()
        self.map[block.hash] = block
        self.last = block

    def print_blockchain(self):
        print('Blockchain in reversed order:')
        block = self.last
        while block.previous_hash is not None:
            self.print_block(block)
            block = self.map[block.previous_hash]
        # if block.previous_hash is None:
        self.print_block(block)


    def print_block(self, block):
        print('timestamp: {}\ndata: {}\nprevious hash: {}\ncurrent hash: {}\n'.format(
            block.timestamp,
            block.data,
            block.previous_hash,
            block.hash))
        time.sleep(0.1)



# Create a blockchain
my_blockchain = Blockchain()

# Generate root block
my_data = "First added block"

root = Block(my_data)
# add the root block to the chain
my_blockchain.append(root)

# Generate second block
my_data = "Second added block"
block = Block(my_data)

# add the second block to the chain
my_blockchain.append(block)

# Generate third block
my_data = "Third added block"
block = Block(my_data)

# add the third block to the chain
my_blockchain.append(block)
my_blockchain.print_blockchain()