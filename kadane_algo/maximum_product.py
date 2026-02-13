"""
152. Maximum Product Subarray
"""
class Solution:
    def maxProduct(self, nums) -> int:
        max_product = nums[0]
        min_product = nums[0]
        

        for num in nums[1:]:
            max_current = max(num, num*max_current)
            max_global = max(max_global, max_current)

        return max_global


assert Solution().maxProduct([2,3,-2,4]) == 6
assert Solution().maxProduct([-2,0,-1]) == 0
assert Solution().maxProduct([-2,3,-4]) == 24