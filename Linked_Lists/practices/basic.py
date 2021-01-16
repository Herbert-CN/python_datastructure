class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    head = None

    def __init__(self, int_list_para: list[int]) -> None:  # build a Linked list from a int list
        for i in range(len(int_list_para)):
            if i == 0:
                self.head = ListNode(val=int_list_para)
                prev = self.head
            else:
                node = ListNode(val=int_list_para[i])
                prev.next = node
                prev = node
        prev.next = None

    def traverse(self):
        cur = self.head
        while cur:
            print(cur.val, end=' ')









