"""
206. Reverse Linked List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # None-1-2-3-4-5
        #      5-4-3-2-1

        prev = None # 2
        curr = head # 3

        while curr:
            next_node = curr.next #4 
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev




assert Solution().reverseList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
)  # == ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))) 
# assert Solution().reverseList(None)  # == None
# assert Solution().reverseList(ListNode(1))  # == ListNode(1)
# assert Solution().reverseList(
#     ListNode(1, ListNode(2))
# )  # == ListNode(2, ListNode(1))
# assert Solution().reverseList(
#     ListNode(1, ListNode(2, ListNode(3)))
# )  # == ListNode(3, ListNode(2, ListNode(1)))