"""
160. Intersection of Two Linked Lists
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0,next=None):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        p1 = headA
        p2 = headB
        
        while p1!=p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


sol = Solution().getIntersectionNode(
    ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))),
    ListNode(5, ListNode(0, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))))
# ) == ListNode(8, ListNode(4, ListNode(5)))  # Intersected at '8'    

# assert Solution().getIntersectionNode(
#     ListNode(1, ListNode(9, ListNode(1, ListNode(2, ListNode(4))))),
#     ListNode(3, ListNode(2, ListNode(4))),
# ) == ListNode(2, ListNode(4))  # Intersected at '2'

# assert Solution().getIntersectionNode(
#     ListNode(2, ListNode(6, ListNode(4))),  
#     ListNode(1, ListNode(5)),
# ) == None  # No intersection