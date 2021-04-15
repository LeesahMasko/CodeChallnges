# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # corner case: if head or head.next == null, return head
        if head is None or head.next is None:
            return head

        # need to keep track of three nodes using three pointers: prev, curr, next
        prev = None
        curr = head
        next = head.next

        # step 1: while curr is not null, reverse prev and curr
        while curr is not None:
            curr.next = prev

            # step 2: increment pointers
            prev = curr
            curr = next

            if next is not None:
                next = next.next

        # step 3: set prev as new head and return it
        head = prev
        return head
