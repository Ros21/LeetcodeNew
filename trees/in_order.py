"""
94. Binary Tree Inorder Traversal
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result


assert Solution().inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))) == [1,3,2]
assert Solution().inorderTraversal(None) == []
assert Solution().inorderTraversal(TreeNode(1)) == [1]
