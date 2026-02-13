"""
47. Permutations II
"""
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        def backtrack(start,path):
            result.append(path[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0,[])
        return result


print(Solution().permuteUnique([1,1,2])) # == [[1,1,2],[1,2,1],[2,1,1]]
print(Solution().permuteUnique([1,2,3])) # == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 
print(Solution().permuteUnique([2,2,1,1])) # == [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
