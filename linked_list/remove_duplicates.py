"""
82. Remove Duplicates from Sorted List II
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
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
            
        print(to_list(dummy.next))    
        return dummy.next
            


sol = Solution().deleteDuplicates(
ListNode(1, ListNode(2, ListNode(3, 
ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))))
# ListNode(1, ListNode(2, ListNode(3, 
# ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))))
# ) == ListNode(1, ListNode(2, ListNode(5)))  # 1->2->3->3->4->4->5 = 1->2->5
# assert Solution().deleteDuplicates(
#     ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
# ) == ListNode(2, ListNode(3))  # 1->1->1->2->3 = 2->3       
# assert Solution().deleteDuplicates(
#     ListNode(1, ListNode(1))
# ) == None  # 1->1 = None    
