"""
1161. Maximum Level Sum of a Binary Tree
"""
# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        level = 1
        answer =1
        max_sum = float("-inf")

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum+= node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum>max_sum:
                max_sum = level_sum
                answer = level

            level+=1
        return answer


print(Solution().maxLevelSum(TreeNode(
    1,
    TreeNode(
        7,
        TreeNode(7),
        TreeNode(-8)
    ),
    TreeNode(
        99,
        TreeNode(3),
        TreeNode(7)
    )
))) #9