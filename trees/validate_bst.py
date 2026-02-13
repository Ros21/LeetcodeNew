"""
98. Validate Binary Search Tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        def valid(node, left,right):
            if not node:
                return True

            if not left<node.val<right:
                return False
            
            return (valid(node.left, left, node.val) and 
            valid(node.right,node.val, right ))

        return valid(root, float("-inf"), float("inf"))
        

assert Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))) == True
assert Solution().isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))) == False
assert Solution().isValidBST(TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))) == False
assert Solution().isValidBST(TreeNode(3, TreeNode(1), TreeNode(5, TreeNode(4), TreeNode(6)))) == True
assert Solution().isValidBST(TreeNode(1, TreeNode(1))) == False
