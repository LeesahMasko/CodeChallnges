class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # corner case: if head or head.next is null, return head
        if head is None or head.next is None:
            return head

        follower = head
        leader = head
        # step 2: move follower and leader pointers until leader.next or leader.next.next is null
        while leader.next is not None and leader.next.next is not None:
            follower = follower.next
            leader = leader.next.next

        # step 3:

        middle = head
        # odd case
        # if leader.next is null, middle is follower
        if leader.next is None:
            middle = follower
        # even case
        # else leader.next.next is null, middle is follower.next
        else:
            middle = follower.next

        return middle
