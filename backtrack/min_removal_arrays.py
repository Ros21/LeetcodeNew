"""
3634. Minimum Removals to Balance Array
"""
from bisect import bisect_right
from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_keep = 0
        for i, num in enumerate(nums):
            j= bisect_right(nums,k*num)
            max_keep = max(max_keep, j-i)
        return len(nums)-max_keep



print(Solution().minRemoval([2,1,5], 2))  # 1
print(Solution().minRemoval([1,6,2,9], 3))  # 2