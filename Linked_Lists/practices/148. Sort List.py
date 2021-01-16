"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?



Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""


# Definition for singly-linked list.
from base_data_structures.leetcode_others.LinkedList.basic import LinkedList, ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        fast = slow.next
        slow.next = None

        head1 = self.sortList(slow)
        head2 = self.sortList(fast)

        # Merge the two sorted list1
        if head1.val < head2.val:
            new_head = cur = head1
            head1 = head1.next
        else:
            new_head = cur = head2
            head2 = head2.next

        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                cur = head1
                head1 = head1.next
            else:
                cur.next = head2
                cur = head2
                head2 = head2.next
        return new_head



if __name__ == '__main__':
    data = LinkedList([-1,5,3,4,0])

    test = Solution()
    test.sortList(data.head)

