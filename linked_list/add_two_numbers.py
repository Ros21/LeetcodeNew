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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total //10
            curr.next = ListNode(total%10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next


ans = Solution().addTwoNumbers(
    ListNode(2, ListNode(4, ListNode(3))),
    ListNode(5, ListNode(6, ListNode(4))))
# ) == ListNode(7, ListNode(0, ListNode(8)))  # 342 + 465 = 807
print(to_list(ans))


ans =  Solution().addTwoNumbers(
    ListNode(0),
    ListNode(0))
# ) == ListNode(0)  # 0 + 0 = 0
print(to_list(ans))


ans =  Solution().addTwoNumbers(
    ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
    ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
# )== ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(1)))))))  
# # 9999999 + 9999 = 10009998
print(to_list(ans))
