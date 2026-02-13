"""
53. Maximum Subarray
"""
class Solution:
    def maxSubArray(self, nums) -> int:
        max_current = nums[0]
        max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num,max_current+num)
            max_global = max(max_global, max_current)
        return max_global


assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert Solution().maxSubArray([1]) == 1
assert Solution().maxSubArray([5,4,-1,7,8]) == 23
assert Solution().maxSubArray([-1]) == -1