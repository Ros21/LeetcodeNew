"""
3010. Divide an Array Into Subarrays With Minimum Cost I
"""
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        rest = sorted(nums[1:])
        return nums[0]+rest[0]+rest[1]


print(Solution().minimumCost([1,2,3,12]))  # 6
print(Solution().minimumCost([5,4,3]))  # 12
print(Solution().minimumCost([10,3,1,1]))  # 12

