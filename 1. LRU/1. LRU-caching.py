class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        if self.value is None:
            return 'None'
        return str(self.value)


class LruCache(object):

    def __init__(self, capacity):
        print('Cache initiated with a capacity of:', capacity)
        self.items = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        node = self.items.get(key, None)
        print('\n\nGet Element with Key:', key, '\nHead:', self.head, '\nTail:', self.tail, '\nItems:', self.items)
        if node is None:
            return -1

        if node.prev is not None:
            self.items[node.prev].next = node.next
        else:
            print('Updating tail with key:', key)
            self.tail = node.next
        if node.next is not None:
            self.items[node.next].prev = node.prev

        head = self.items.get(self.head, None)
        if head is not None:
            head.next = key

        node.prev = self.head
        node.next = None

        self.head = key
        return node

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        head = self.items.get(self.head, None)
        new_node = Node(value)

        if self.capacity == 0:
            print('Cannot perform operations on 0 capacity cache')
            return

        if head is None:
            self.head = key
            self.tail = key
        else:
            new_node.prev = self.head
            head.next = key

        self.items[key] = new_node
        self.head = key

        if len(self.items) > self.capacity:
            print('\n--- Capacity Exceeded, deleting', self.tail)
            tail = self.items[self.tail]  # no possible to get a KeyException
            del self.items[self.tail]
            self.tail = tail.next


if __name__ == '__main__':
    our_cache = LruCache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    our_cache.get(1)  # returns 1
    our_cache.get(2)  # returns 2
    our_cache.get(9)  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used
    print(our_cache.get(5))  # should return 5
    print(our_cache.get(6))  # should return 6

    print(our_cache.items)
    print(our_cache.head)

    our_cache.set(7, 9009)
    our_cache.set(8, 1)
    our_cache.set(6, 9)  # least recently used not deleted because 6 updates, does not add a new one
    our_cache.set(3, 100)

    print(our_cache.items)

    our_cache = LruCache(0)
    our_cache.set(1, 1)
    print(our_cache.get(1))
