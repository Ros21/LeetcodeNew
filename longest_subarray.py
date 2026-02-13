"""
3719. Longest Balanced Subarray I
"""
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_length = 0
        for i in range(len(nums)):
            even_set = set()
            odd_set = set()
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])
                if len(even_set)==len(odd_set):
                    max_length = max(max_length, j-i+1)
        return max_length


print(Solution().longestBalanced([2,5,4,3]))  # 4
print(Solution().longestBalanced([3,2,2,5,4]))  # 5
print(Solution().longestBalanced([1,2,3,2]))  # 3
