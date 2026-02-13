"""
61. Rotate List
"""
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
    def rotateRight(self, head, k: int):
        if not head or k==0 or not head.next:
            return head

        length = 1
        tail = head
        while tail.next:
            length+=1
            tail = tail.next

        tail.next = head

        tail_step = length - (k%length)-1

        new_tail = head
        for _ in range(tail_step):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head



assert Solution().rotateRight(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
) == ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))  # 1->2->3->4->5 rotated by 2 = 4->5->1->2->3
assert Solution().rotateRight(
    ListNode(0, ListNode(1, ListNode(2))), 4
) == ListNode(2, ListNode(0, ListNode(1)))  # 0->1->2 rotated by 4 = 2->0->1
assert Solution().rotateRight(
    None, 0
) == None  # Empty list rotated by 0 = Empty list
assert Solution().rotateRight(
    ListNode(1), 99
) == ListNode(1)  # 1 rotated by 99 = 1
