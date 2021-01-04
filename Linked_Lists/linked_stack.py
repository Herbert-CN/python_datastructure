class LinkedStack:
    """Linked stack"""
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element):
            self._element = element
            self._next = None

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def put(self, element):
        """Put an element to the linked stack"""
        new_node = self._Node(element)
        new_node._next = self._head
        self._head = new_node
        self._size += 1

    def search(self, element):
        """Find an element in the linked stack"""
        cur = self._head
        while cur.next:
            if cur._element == element:
                return True
        return False

    def pop(self):
        """Pop head of linked stack"""
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            self._head = self._head._next
            self._size -= 1

    def get_top(self):
        """Return the top element"""
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return self._head._element

    def traverse(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            cur = self._head
            while cur._next:
                print(f"{cur._element}->", end='')
                cur = cur._next

            print(f"{cur._element}")

    def reverse(self):
        if self.is_empty():
            return None
        else:
            prev, cur = None, self._head
            while cur:
                cur = cur._next
                self._head._next = prev
                prev = self._head
                # self._head = cur
                if cur:
                    self._head = cur

                    
    def reverse_v2(self):
        if self.is_empty():
            return None
        else:
            prev, cur = self._head, self._head._next
            while cur:
                self._head._next = cur._next
                cur._next = prev
                prev = cur
                cur = self._head._next
            self._head = prev






if __name__ == '__main__':
    mylinkedstack = LinkedStack()
    mylinkedstack.put("A")
    mylinkedstack.put("B")
    mylinkedstack.put("C")
    mylinkedstack.traverse()

    mylinkedstack.reverse_v2()
    mylinkedstack.traverse()





