# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1, None)
        curr_sorted = dummy_head

        while list1 and list2:
            if list1.val <= list2.val:
                curr_sorted.next = list1
                list1 = list1.next
            else:
                curr_sorted.next = list2
                list2 = list2.next

            curr_sorted = curr_sorted.next

        if list1:
            curr_sorted.next = list1
        else:
            curr_sorted.next = list2

        return dummy_head.next
        