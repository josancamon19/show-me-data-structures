import hashlib
from datetime import datetime


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.utcnow()
        self.data = data
        self.hash = self.calc_hash()
        self.previous_hash = previous_hash

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.blocks = {}
        self.head = None

    def append(self, block):
        self.head = block
        self.blocks[block.hash] = block

    def get_hash(self, hash_value):
        return self.blocks.get(hash_value, None)

    def size(self):
        if self.head is None:
            return 0

        current = self.blocks.get(self.head, None)
        size = 1 if current else 0
        while current:
            current = self.blocks.get(current.previous_hash)
            size += 1

        return size
