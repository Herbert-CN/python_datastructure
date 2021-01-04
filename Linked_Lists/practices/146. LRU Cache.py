class LRUCache:

    class _Node:
        __slots__ = '_key', '_value', '_next'

        def __init__(self, key, value):
            self._key = key
            self._value = value
            self._next = None

    def __init__(self, capacity: int):
        self._head = None
        self._size = 0
        self._capacity = capacity

    def get(self, key: int) -> int:
        prev = cur = self._head
        if not self._size:  # Empty LRU
            return -1
        if self._head._key == key:  # The node to find is the head
            return self._head._value
        else:
            while cur:
                if cur._key == key:  # Delete the node and add it to the head
                    prev._next = cur._next
                    self._size -= 1
                    self._enqueue(cur._key, cur._value)
                    return cur._value
                else:
                    prev, cur = cur, cur._next
            return -1

    def put(self, key: int, value: int) -> None:
        prev = cur = self._head
        new_node = self._Node(key, value)
        if not self._size:  # Empty LRU
            self._enqueue(key, value)
        if self._head._key == key:  # The node to find is the head
            self._head._value = value
        else:
            found = False
            while cur:
                if cur._key == key:  # Update value, delete the node and add it to the head
                    cur._value = value # Update the value
                    prev._next = cur._next
                    self._size -= 1
                    self._enqueue(cur._key, cur._value)
                    found = True
                    break
                else:
                    prev, cur = cur, cur._next
            if not found:
                if self._size < self._capacity:
                    self._enqueue(key, value)
                else:
                    self._dequeue()
                    self._enqueue(key, value)

    def _enqueue(self, key, value):
        new_node = self._Node(key, value)
        if not self._size: # Empty LRU
            self._head = new_node
        else:
            new_node._next = self._head
            self._head = new_node
        self._size += 1

    def _dequeue(self):
        """Remove the last node in the LRU without return"""
        if not self._size: # Empty LRU
            raise Exception('Empty LRU Cache')
        elif self._size == 1:
            self._head = None
        else:
            prev = cur = self._head
            while cur._next:
                prev, cur = cur, cur._next
            prev._next = None
        self._size -= 1


if __name__ == '__main__':
    lru_cache = LRUCache(2)
    lru_cache.put(2, 1)
    lru_cache.put(1, 1)
    lru_cache.put(2, 3)
    lru_cache.put(4, 1)
    print(lru_cache.get(1))
    print(lru_cache.get(2))
