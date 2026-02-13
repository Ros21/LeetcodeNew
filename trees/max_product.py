"""
1339. Maximum Product of Splitted Binary Tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root) -> int:
        MOD = 10**9+7
        self.max_product = 0
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left)+ total_sum(node.right)

        total = total_sum(root)

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            subtree_sum = node.val+left+right

            self.max_product = max(self.max_product, 
            subtree_sum*(total-subtree_sum
            ))

            return subtree_sum

        dfs(root)
        return self.max_product % MOD

    
print(Solution().maxProduct(
    TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6))
    )
))#== 110

# assert Solution().maxProduct(
#     TreeNode(
#         2,
#         TreeNode(3, TreeNode(10), TreeNode(7)),
#         TreeNode(9, TreeNode(8), TreeNode(6))
#     )
# ) == 495

assert Solution().maxProduct(
    TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                3,
                TreeNode(4)
            )
        )
    )
) == 24

assert Solution().maxProduct(
    TreeNode(
        1,
        None,
        TreeNode(
            2,
            None,
            TreeNode(
                3,
                None,
                TreeNode(4)
            )
        )
    )
) == 24