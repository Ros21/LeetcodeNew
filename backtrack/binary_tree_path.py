"""
257. Binary Tree Paths
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        result = []

        def dfs(node, path):

            path+=str(node.val)
            if not node.left and not node.right :
                result.append(path)

            
            if node.left:
                dfs(node.left, path + "->")
            if node.right:
                dfs(node.right, path + "->")

        dfs(root,"")
        return result

print(Solution().binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3)))) # == ["1->2->5", "1->3"]
# assert Solution().binaryTreePaths(TreeNode(1)) == ["1"]
# assert Solution().binaryTreePaths(None) == []
# assert Solution().binaryTreePaths(TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4)))) == ["1->2", "1->3->4"]


