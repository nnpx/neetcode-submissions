# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        # If no cycle, fast will reach the end (null) and the loop stops.
        # To evaluate fast.next.next, fast and fast.next must not be None (so accessing .next is valid)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
        