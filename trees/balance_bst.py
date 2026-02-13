"""
1382. Balance a Binary Search Tree
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            result.append(node.val)
            in_order(node.right)

        def build_bst(l,r):
            if l>r:
                return None
            mid = (l+r)//2
            print(l, r, mid, result[mid])
            node = TreeNode(result[mid]) 
            node.left = build_bst(l,mid-1)
            print("Called")
            node.right = build_bst(mid+1,r)
            return node
                
        in_order(root)
        return build_bst(0, len(result)-1)


print(Solution().balanceBST(TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4)))))) # [2,1,3,null,null,null,null,4]
# print(Solution().balanceBST(TreeNode(2, TreeNode(1), TreeNode(3, None, TreeNode(4))))) # [3,2,4,1]