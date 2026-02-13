"""
783. Minimum Distance Between BST Nodes
530. Minimum Absolute Difference in BST
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root) -> int:
        self.prev = None
        self.min_diff = float("inf")

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff
            

assert Solution().minDiffInBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))) == 1
assert Solution().minDiffInBST(TreeNode(1, None, TreeNode(3, TreeNode(2)))) == 1
assert Solution().minDiffInBST(TreeNode(27, TreeNode(14, None, TreeNode(19, TreeNode(17), TreeNode(22))), TreeNode(38, TreeNode(34), TreeNode(48)))) == 2
