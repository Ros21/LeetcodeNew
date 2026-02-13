"""
144. Binary Tree Preorder Traversal
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return 
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result


assert Solution().preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))) == [1,2,3]
assert Solution().preorderTraversal(None) == []
assert Solution().preorderTraversal(TreeNode(1)) == [1]
