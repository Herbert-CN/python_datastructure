"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head
        i = 0

        # 让快指针先走n步
        while i < n:
            fast = fast.next
            i += 1

        # 快慢指针一起走，fast走到终点，slow就是要删除的位置
        while fast.next:
            slow = slow.next
            fast = fast.next

        #删除该位置
        slow.next = slow.next.next

        return head



