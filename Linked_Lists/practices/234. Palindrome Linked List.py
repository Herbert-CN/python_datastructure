class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        prev, fast, slow = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            head = slow.next
            slow.next = prev
            prev, slow = slow, head

        # 通过fast 和 fast.next 来判断长度为奇数还是偶数
        if fast: # fast 不为None，奇数个
            head = head.next

        # prev 是前半段的head, head, slow 是后半段的head
        while head:
            if head.val != prev.val:
                return False
            else:
                head, prev = head.next, prev.next
        return True
