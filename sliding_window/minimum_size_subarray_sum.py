"""
209. Minimum Size Subarray Sum
"""
class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        left = 0
        window_sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            window_sum+=nums[right]

            while window_sum>=target:
                min_length = min(min_length, right-left+1)
                window_sum-=nums[left]
                left+=1
        
        return 0 if min_length== float('inf') else min_length


assert Solution().minSubArrayLen(7, [2,3,1,2,4,3]) == 2
assert Solution().minSubArrayLen(4, [1,4,4]) == 1
assert Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0    
