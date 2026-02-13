"""
92. Reverse Linked List II
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(node):
    elem = []
    while node:
        elem.append(node.val)
        node = node.next
    return elem


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1-2-3-4-5      2,4
        # 1-4-3-2-5
        if left ==right:
            return head
        
        dummy = ListNode(0, head)
        left_prev = dummy

        for _ in range(left-1):
            left_prev = prev.next #1

        current = left_prev.next #2
        prev = None
        print(f"current: {current.val}, prev : {prev.val}")

        for _ in range(right-left+1):
            next_node = current.next #3
            current.next = prev
            
            print(f"{next_node.val}, {current.next.val}, {prev.next.val}")
        print(to_list(dummy.next))
        return dummy.next




assert Solution().reverseBetween(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4
)   == ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5))))) 
# assert Solution().reverseBetween(None, 1, 1)  # == None
# assert Solution().reverseBetween(ListNode(1), 1, 1)  # == ListNode(1)
# assert Solution().reverseBetween(
#     ListNode(1, ListNode(2)), 1, 2
# )  # == ListNode(2, ListNode(1))