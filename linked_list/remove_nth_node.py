"""
19. Remove Nth Node From End of List
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        # print(to_list(dummy.next))
        return dummy.next



assert Solution().removeNthFromEnd(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
) == ListNode(1, ListNode(2, ListNode(3, ListNode(5))))  # 1->2->3->4->5, remove 2nd from end = 1->2->3->5
# assert Solution().removeNthFromEnd(
#     ListNode(1), 1
# ) == None  # 1, remove 1st from end = None
# assert Solution().removeNthFromEnd(
#     ListNode(1, ListNode(2)), 1
# ) == ListNode(1)  # 1->2, remove 1st from end = 1   
