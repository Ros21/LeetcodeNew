"""
234. Palindrome Linked List
"""
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        listnode_str = ""
        while head:
            listnode_str += str(head.val)
            head = head.next

        if listnode_str == "".join(reversed(listnode_str)):
            return True
        else:
            return False


assert Solution().isPalindrome(
    ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
)  # == True
assert not Solution().isPalindrome(
    ListNode(1, ListNode(2))
)  # == False

assert Solution().isPalindrome(
    ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
)  # == True