"""
103. Binary Tree Zigzag Level Order Traversal
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            left_to_right = not left_to_right
            result.append(level)
        return result




assert Solution().zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [[3], [20, 9], [15, 7]]
assert Solution().zigzagLevelOrder(TreeNode(1)) == [[1]]
assert Solution().zigzagLevelOrder(None) == []