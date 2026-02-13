"""
101. Symmetric Tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        def is_mirror(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            return is_mirror(left.left,right.right)\
                and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)


assert Solution().isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))) == True
assert Solution().isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))) == False
assert Solution().isSymmetric(None) == True
assert Solution().isSymmetric(TreeNode(1)) == True