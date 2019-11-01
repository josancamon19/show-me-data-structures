import hashlib
from datetime import datetime


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


def next_block(last_block):
    if last_block is None or type(last_block) is not Block:
        print("Invalid Last block")
        return
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = "I'm block {}".format(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


if __name__ == '__main__':
    chain = [Block(0, datetime.now(), "First Block", "0")]
    for i in range(0, 10):
        chain.append(next_block(chain[-1]))

    for block in chain:
        print(block.data)
