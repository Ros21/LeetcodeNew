"""
78. Subsets
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def bactrack(path):
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    bactrack(path)
                    path.pop()
                    used[i] = False
                subset = sorted(path[:])
                if subset not in result:
                    result.append(subset)
            
        bactrack(path)
        return result


print(Solution().subsets([1,2,3,4,5,6,7,8,10,0]))