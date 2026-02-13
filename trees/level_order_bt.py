"""
102. Binary Tree Level Order Traversal
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        result = []
        if not root:
            return result

        q = deque([root])
        while q:
            level = []
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
      
        return result
            


assert Solution().levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [[3], [9, 20], [15, 7]]
assert Solution().levelOrder(TreeNode(1)) == [[1]]
assert Solution().levelOrder(None) == []
assert Solution().levelOrder(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))) == [[1], [2, 3], [4, 5]]

   
