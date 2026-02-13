"""
78. Subsets
"""
from typing import List

class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # subset = []

        # def backtrack(i):
        #     if i == len(nums):
        #         res.append(subset.copy())
        #         return
            
        #     # include nums[i]
        #     subset.append(nums[i])
        #     backtrack(i + 1)

        #     # exclude nums[i]
        #     subset.pop()
        #     backtrack(i + 1)

        # backtrack(0)
        # return res


    def subsets(self, nums):
        res = [[]]
        for num in nums:
            new_subsets = [current+[num] for current in res]
            res.extend(new_subsets)
        return res


print(Solution().subsets([1,2,3]))