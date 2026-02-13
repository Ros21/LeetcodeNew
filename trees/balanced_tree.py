"""
110. Balanced Binary Tree
"""
from typing import List, Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            if left == -1:
                return -1
            
            right = height(node.right)
            if right == -1:
                return -1

            if abs(left-right)>1:
                return -1
            
            return 1+max(left,right)
        
        return height(root)!=-1

print(Solution().isBalanced(TreeNode(3,TreeNode(9),TreeNode(20,                                                         
    TreeNode(15), TreeNode(7))))) #true
print(Solution().isBalanced(TreeNode(1,
    TreeNode(2,
        TreeNode(3, TreeNode(4), TreeNode(4)),
        TreeNode(3)
    ),
    TreeNode(2)
))) #false
print(Solution().isBalanced(None)) #true

"""

        1
       / \
      2   2
     / \
    3   3
   / \
  4   4

  """