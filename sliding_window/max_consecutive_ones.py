"""
485. Max Consecutive Ones
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for right in range(len(nums)):
            if nums[right]==0:
                count = 0
            else:
                count+=1
                max_count = max(count, max_count)
        return max_count
                



assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
assert Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]) == 2
assert Solution().findMaxConsecutiveOnes([0,0,0]) == 0
