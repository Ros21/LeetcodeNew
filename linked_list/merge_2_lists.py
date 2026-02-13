"""
21. Merge Two Sorted Lists
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        final_list = dummy

        while list1 and list2:
            if list1.val<=list2.val:
                final_list.next = list1
                list1 = list1.next 
            else:
                final_list.next = list2
                list2 = list2.next 
                
            final_list = final_list.next

        final_list.next = list1 if list1 else list2

        return dummy.next

        


assert Solution().mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4))),
    ListNode(1, ListNode(3, ListNode(4)))
)  == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))



