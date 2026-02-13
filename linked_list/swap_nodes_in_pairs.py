"""
24. Swap Nodes in Pairs
"""

# Definition for singly-linked list.
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
    def swapPairs(self, head):
        # dummy -> first -> second
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first

            prev = first

        return dummy.next



assert Solution().swapPairs(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
) == ListNode(2, ListNode(1, ListNode(4, ListNode(3))))  # 1->2->3->4 = 2->1->4->3

# assert Solution().swapPairs(
#     ListNode()
# ) == ListNode()  # Empty list   

# assert Solution().swapPairs(
#     ListNode(1)
# ) == ListNode(1)  # 1 = 1   

# assert Solution().swapPairs(
#     ListNode(1, ListNode(2, ListNode(3)))
# ) == ListNode(2, ListNode(1, ListNode(3)))  # 1->2->3 = 2->1->3
        