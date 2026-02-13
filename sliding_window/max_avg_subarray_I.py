"""
643. Maximum Average Subarray I
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        current_sum = max_sum
        for num in range(k,len(nums)):
            current_sum = current_sum +nums[num]- nums[num-k]
            max_sum = max(max_sum, current_sum)
        return round(max_sum/k, 5)




# assert Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75    
# assert Solution().findMaxAverage([5], 1) == 5.0
# assert Solution().findMaxAverage([0, 4, 0, 3, 2], 1) == 4.0
# assert Solution().findMaxAverage([-1], 1) == -1.0
# assert Solution().findMaxAverage([1, -1], 2) == 0.0
assert Solution().findMaxAverage([4,2,1,3,3], 2) == 3.00000