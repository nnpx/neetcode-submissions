# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # separate linked list into half half -> [...slow] [second...] 
        # e.g, [2,4,6,8,10] -> [2,4,6] [8,10]
        slow = head
        fast = head.next # ensure that for an even-length list, slow stops at the end of the first half rather than the start of the second half.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # `second` is start of second half
        prev = None
        slow.next = None # first half ends at slow

        # reverse second half e.g, [2,4,6] [8,10] -> [2,4,6] [10,8]
        while second:
            temp_next = second.next
            second.next = prev
            prev = second
            second = temp_next
        
        # connect first node of `first` then first node of `second` 
        # e.g, [2,4,6] [10,8] -> [2,10,4,8,6]
        first = head
        second = prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2



        